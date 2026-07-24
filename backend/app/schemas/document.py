from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class DocumentBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: Optional[str] = None
    language: str = Field(default="ko")
    dynasty: Optional[str] = None
    source: Optional[str] = None


class DocumentCreate(DocumentBase):
    project_id: int


class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    dynasty: Optional[str] = None
    source: Optional[str] = None


class DocumentUploadResponse(BaseModel):
    id: int
    filename: str
    message: str


class DocumentSummary(BaseModel):
    id: int
    title: str
    dynasty: Optional[str]

    model_config = ConfigDict(from_attributes=True)
