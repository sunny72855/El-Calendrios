const generatorButton = document.getElementById('generate-btn');
const addButton = document.getElementById('add-task-btn')
let taskList = [
    { day: "Monday", tasks: [] },
    { day: "Tuesday", tasks: [] },
    { day: "Wednesday", tasks: [] },
    { day: "Thursday", tasks: [] },
    { day: "Friday", tasks: [] },
    { day: "Saturday", tasks: [] },
    { day: "Sunday", tasks: [] }
];

generatorButton.addEventListener('click', async () => {
    const context = document.getElementById('rawText').value;
    const intensity = document.getElementById('intensity').value;
    const focus = document.getElementById('focus').value;

    const jsonString = {
            rawText: context,
            intensityMode: intensity,
            focusStyle: focus,
            existingSchedule: taskList // Pass the actual array variable here
    };

    // Check if frontend died + main logic
    try {
        const response = await fetch("http://127.0.0.1:8000/api/schedule/", {
            method: "POST",
            headers: {

                "Content-Type": "application/json"
            },
            body: JSON.stringify(jsonString)
        });

        // Check if backend died
        if (!response.ok) {
            const errorDetails = await response.json();

            throw new Error(`Backend imploded D: (${response.status}): ${JSON.stringify(errorDetails)}`);
        }

        const result = await response.json();
        taskList = result;
        renderCalendar();
        console.log("Success :D");
    } catch (error) {
        console.error("Network error D: ", error);
    }
})

addButton.addEventListener('click', () => {
    const targetDay = document.getElementById('fixedDay').value;
    const title = document.getElementById('fixedTitle').value.trim();
    const startTime = document.getElementById('fixedStart').value;
    const endTime = document.getElementById('fixedEnd').value;

    if (!title || !startTime || !endTime) {
        alert("Please fill out all task details!");
        return;
    }

    if (timeToMinutes(startTime) >= timeToMinutes(endTime)) {
        alert("End time must be after the start time!");
        return;
    }

    const dayData = taskList.find(d => d.day === targetDay);
    
    if (dayData) {
        dayData.tasks.push({
            title: title,
            time: `${startTime} - ${endTime}`,
            type: "fixed" 
        });

        sortTasksChronologically(dayData.tasks);

        renderCalendar(taskList);

        document.getElementById('fixedTitle').value = '';
        document.getElementById('fixedStart').value = '';
        document.getElementById('fixedEnd').value = '';
    }
});

function renderCalendar() {

    if (taskList.length === 0) {
        return;
    }

    taskList.forEach(dayData => {
        const dayColumn = document.getElementById(dayData.day);
        const taskListContainer = dayColumn.querySelector('.task-list');

        taskListContainer.innerHTML = '';

        dayData.tasks.forEach(task => {
            const taskDiv = document.createElement('div');

            taskDiv.classList.add('task');

            if (task.type === 'ai-generated') {
                taskDiv.style.borderLeftColor = '#2563eb'; // Blue accent for AI
                taskDiv.style.background = '#eff6ff';
            } else {
                taskDiv.style.borderLeftColor = '#2c0472'; // Purple accent for Fixed
                taskDiv.style.background = '#eef2ff';
            }

            taskDiv.innerHTML = `
                <strong>${task.title}</strong>
                <div class="small muted">${task.time}</div>
            `;

            taskListContainer.appendChild(taskDiv);
        });
    });

    console.log(taskList);
}

// THE HANDLERS
// VERY important for calculating placement logic
function timeToMinutes(timeStr) {
    const [hours, minutes] = timeStr.split(':').map(Number);
    return hours * 60 + minutes;
}

function sortTasksChronologically(tasksArray) {
    return tasksArray.sort((taskA, taskB) => {

        // Extract the start time
        const startTimeA = taskA.time.split(' - ')[0];
        const startTimeB = taskB.time.split(' - ')[0];

        // Compare their total minutes from midnight
        return timeToMinutes(startTimeA) - timeToMinutes(startTimeB);
    });
}