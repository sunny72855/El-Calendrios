from pydantic import BaseModel

class CalendarTask(BaseModel):
    time: str        # e.g., "13:00 - 15:30"
    title: str       # e.g., "Deep Work: Rotational Dynamics FRQs"
    type: str        # "fixed" or "ai-generated"

class DailySchedule(BaseModel):
    day: str         # e.g., "Monday"
    tasks: list[CalendarTask]