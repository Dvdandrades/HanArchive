from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AnalysisType(str, Enum):
    TOKENIZATION = "tokenization"
    NER = "ner"
    TIMELINE = "timeline"
    EMBEDDINGS = "embeddings"
    NETWORK = "network"
    COMPLETE = "complete"


class AnalysisStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"


class AnalysisRequest(BaseModel):
    document_id: int
    analysis_type: AnalysisType


class AnalysisResponse(BaseModel):
    task_id: str
    status: AnalysisStatus


class AnalysisResult(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    document_id: int
    analysis_type: AnalysisType
    status: AnalysisStatus
    started_at: Optional[datetime]
    finished_at: Optional[datetime]
    execution_time: Optional[float]
    model_name: Optional[str]
    message: Optional[str]


class AnalysisStatistics(BaseModel):
    documents_processed: int
    total_tokens: int
    entities_found: int
    persons_found: int
    locations_found: int
    events_found: int
    average_execution_time: float
