from pydantic import BaseModel, ConfigDict
from datetime import datetime

class DocumentCreate(BaseModel):
    title: str
    language: str
    original_text: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    language: str
    original_text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)