from pydantic import BaseModel
from backend.schemas.calendar_schema import DailySchedule

# Parses frontend JSON into Python objects
class UserPayload(BaseModel):
    rawText: str
    intensityMode: str
    focusStyle: str
    existingSchedule: list[DailySchedule]