from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


# The data user should provide when creating a new research task
class ResearchTaskCreate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    company: str = Field(min_length=1, max_length=100)
    question: str = Field(min_length=3, max_length=2000)
    cutoff_date: date


# The data returned by the API after a research task is created successfully
class ResearchTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    company: str
    question: str
    cutoff_date: date
    status: str
    created_at: datetime