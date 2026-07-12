from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas.payload_schema import UserPayload
from backend.engines.llm_engine import generate_schedule

app = FastAPI()

origins = [
    "http://localhost:5500",      # Default VS Code Live Server port
    "http://127.0.0.1:5500",      # Alternate Live Server loopback
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows requests from your frontend origins
    allow_credentials=True,
    allow_methods=["*"],              # Allows all standard methods (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],              # Allows all headers (like Content-Type)
)

@app.post('/schedule/')
async def process_calendar(calendar: UserPayload):
    try:
        response = await generate_schedule(
            calendar.rawText,
            calendar.intensityMode,
            calendar.focusStyle,
            calendar.existingSchedule
        )
        print(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Schedule generation failed: {str(e)}")

