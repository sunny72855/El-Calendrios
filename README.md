# 📅 AI Dynamic Schedule Engine

A lightweight, automated calendar manager built with a **FastAPI** backend and a responsive vanilla JavaScript grid frontend. The engine dynamically evaluates user availability, respects hard-coded user constraints, and optimizes daily schedules based on selectable focus frameworks and intensity styles.

---

## 🚀 System Architecture & Directory Layout

The codebase uses a clean, decoupled structure separating the core backend endpoints from the static client frontend:

├── api/
│   ├── index.py             # Main FastAPI entry point & API Router
│   └── backend/             # Core backend logic container
│       ├── engines/
│       │   └── llm_engine.py # Generation logic
│       └── schemas/
│           ├── calendar_schema.py
│           └── payload_schema.py
├── index.html               # Main frontend interface
├── script.js                # State management, time sorting, & API communications
├── style.css                # Interface layout & styling
├── requirements.txt         # Python platform dependency manifest
└── README.md

# 🛠️ Features
Dynamic Block Generation: Automatically processes raw user requirements via an LLM orchestration layer.

Fixed Task Reservation: Enables users to manually map static weekly commitments (e.g., school hours, practices) directly into the client state.

Deterministic Time Sorting: Utilizes an in-place Timsort configuration to chronologically align calendar cards instantly upon insertion.

Modular Codebase: Clean separation of concerns between API data validation schemas and core processing routines.

### 🔧 Local Development & Setup
Prerequisites

Python 3.9+
Git
A modern web browser

1. Clone & Navigate

git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd AI-Schedule-Engine

2. Configure the Backend Microservice
Set up your Python virtual environment and pull down the strict dependencies:

Initialize and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install package definitions
pip install -r requirements.txt

3. Environment Variables
Create a .env file inside the root directory to store your credentials:

Code snippet
GEMINI_API_KEY=your_api_key_here
Don't change the name to anything but GEMINI_API_KEY otherwise the LLM will not work (learnt this the hard way)

4. Run the Local Servers
To spin up the local Uvicorn development server:

uvicorn api.index:app --reload (remove the --reload if you just want to experience it)
The API documentation will be interactively available at http://127.0.0.1:8000/docs. Open index.html directly in your browser or run it via a local live server extension to interface with the platform.