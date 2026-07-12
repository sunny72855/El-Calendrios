# 📅 AI Dynamic Schedule Engine

An automated calendar manager with a **FastAPI** backend and a responsive vanilla JavaScript grid frontend. The engine evaluates user availability, respects hard-coded constraints, and optimizes daily schedules based on selectable focus frameworks and intensity styles.

---

## ✨ Features

- **Dynamic Block Generation** — processes raw user requirements through an LLM orchestration layer
- **Fixed Task Reservation** — map static weekly commitments (school hours, practices, etc.) directly into client state
- **Deterministic Time Sorting** — in-place Timsort keeps calendar cards chronologically aligned on insertion
- **Modular Codebase** — clean separation between API validation schemas and core processing logic

---

## 🏗️ Architecture

```
├── api/
│   ├── index.py               # FastAPI entry point & API router
│   └── backend/
│       ├── engines/
│       │   └── llm_engine.py  # Generation logic
│       └── schemas/
│           ├── calendar_schema.py
│           └── payload_schema.py
├── index.html                 # Frontend interface
├── script.js                  # State management, time sorting, API calls
├── style.css                  # Layout & styling
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🔧 Getting Started

### Prerequisites

- Python 3.9+
- Git
- A modern web browser

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd AI-Schedule-Engine
```

### 2. Set up the backend

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ The variable **must** be named `GEMINI_API_KEY` — anything else and the LLM engine won't pick it up.

### 4. Run the app

```bash
uvicorn api.index:app --reload
```

Drop `--reload` for a non-dev run.

- API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Frontend: open `index.html` directly, or serve it with a live-server extension

---

## 🧱 Tech Stack

| Layer      | Tech                          |
|------------|--------------------------------|
| Backend    | FastAPI, Python 3.9+           |
| Frontend   | Vanilla JS, HTML, CSS          |
| LLM Engine | Gemini API                     |
| Server     | Uvicorn                        |

---

## 🗺️ Roadmap

- [ ] Persistent storage for saved schedules
- [ ] Auth for multi-user support
- [ ] Additional LLM provider support

## Note

Add http://127.0.0.1:8000/ to the start of api/schedule in script.js if you are hosting backend and frontend seperately