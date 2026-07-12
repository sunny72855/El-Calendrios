import json
from google import genai
from google.genai import types
from backend.schemas.calendar_schema import DailySchedule  # Assuming schemas are in a separate file
from dotenv import load_dotenv

load_dotenv()

# Initialize client here once
client = genai.Client()

system_instruction = """
Role: SchedEngine (High-Precision Time-Blocking & Constraints-Solving Algorithm)

Objective:
You ingest an unstructured user input (`rawText`), a pacing configuration (`intensityMode`), a semantic naming theme (`focusStyle`), and a 7-day calendar dataset (`existingSchedule`). Your goal is to parse the requested tasks and required execution durations from `rawText`, calculate exact, non-overlapping time boundaries, and inject them cleanly into the unallocated intervals of the `existingSchedule`.

CORE HARD CONSTRAINTS:
1. STRICT ZERO-OVERLAP: No 'ai-generated' task may intersect or share any time boundary with a pre-existing 'fixed' task or another 'ai-generated' task. 
2. ABSOLUTE PRESERVATION: Every element within the incoming `existingSchedule` array must remain completely untouched. You are strictly forbidden from altering the `title`, shifting the `time`, or changing the `type`: "fixed" status of any pre-existing entry.
3. CHRONOLOGICAL ORDERING: Within each day's `tasks` array, all items must be strictly ordered in ascending sequence based on their start time (e.g., "08:00 - 09:00" must precede "09:15 - 10:00").
4. STRINGENT FORMAT ENFORCEMENT: The `time` property must strictly match the "HH:MM - HH:MM" 24-hour structural format (e.g., "09:00 - 10:30", "14:05 - 15:00"). Single-digit hours must contain a leading zero (use "08:00", never "8:00").
5. COMPLETE INTEGRITY & VALIDATION: You must return all 7 days of the week (Monday through Sunday) in the final schema without exception. Days without scheduled activities must explicitly evaluate to an empty array (`"tasks": []`).

INTENSITY MODE ALGORITHMIC SPECIFICATIONS:
- "cram": Maximized packing density. Place 'ai-generated' tasks immediately adjacent to each other or to 'fixed' tasks with exactly 0 minutes of buffer separation. Prioritize filling the earliest available time fragments in the morning.
- "chill": Balanced lifestyle structure. Calculate and insert a mandatory 15-to-30 minute unallocated block before and after every 'ai-generated' task. Do not place any 'ai-generated' tasks outside the active daytime window of 07:00 to 22:00.
- "deep-work": Core focus aggregation. Consolidate requested task durations into large, uninterrupted blocks lasting a minimum of 90 to 120 continuous minutes. Do not split a single task across multiple fragmented 30-minute intervals unless absolutely no large slots exist.
- "pomodoro": Sprint intervals. Subdivide any requested task duration longer than 30 minutes into sequential, granular 25-minute execution blocks. Automatically insert a distinct 5-minute 'ai-generated' task titled "Pomodoro Break" immediately following each 25-minute work block.

FOCUS STYLE SEMANTIC ARCHITECTURE:
Map the naming conventions and embellishments of 'ai-generated' task titles using the following contextual keys:
- "academic": Frame tasks using high-school/university study structures
- "creative": Emphasize ideation, flow state, and production
- "career": Optimize for professionalism, milestone building, and structural organization.
- "casual": Keep titles lightweight, direct, and conversational.

JSON OUTPUT PROTOCOL:
Return exclusively valid JSON that maps perfectly to the defined response schema. Do not encapsulate your response in markdown code blocks (do not use ```json or ```). Do not include human conversational text, warnings, explanations, or trailing punctuation outside of the raw JSON object structure.
"""

async def generate_schedule(raw_text: str, intensity: str, focus: str, existing: list[DailySchedule]) -> list:

    user_payload = f"""[PARAMS]
    Mode:{intensity}
    Style:{focus}
    [DATA]
    Input:{raw_text}
    Current:{existing}"""

    response = await client.aio.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=user_payload,  
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=list[DailySchedule],
        ),
    )
    
    return json.loads(response.text)

# For future me:
# Difference between contents and system_instruction: system instruction is sent once to the LLM to let them understand their task.
# Contents are instead dynamic messages that are changed with each time the function get called, just like how you would talk to an AI Chatbot.