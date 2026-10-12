from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from enum import Enum

class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"

class SupportTicket(BaseModel):
    ticket_id: str = Field(..., description="Unique ID for the ticket")
    customer_id: str
    subject: str
    body_text: str
    attachment_type: Optional[str] = Field(None, description="e.g. image, pdf, audio, text")
    metadata: Optional[Dict[str, Any]] = None

class TriageResult(BaseModel):
    ticket_id: str
    priority: PriorityEnum
    assigned_queue: str
    urgency_score: float
    detected_features: List[str] = []
    processing_time_ms: float