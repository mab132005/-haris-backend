from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Blocked Number Schemas
class BlockedNumberBase(BaseModel):
    phone_number: str
    reason: str
    severity: Optional[str] = "خطر شديد"

class BlockedNumberCreate(BlockedNumberBase):
    pass

class BlockedNumberUpdate(BaseModel):
    phone_number: Optional[str] = None
    reason: Optional[str] = None
    severity: Optional[str] = None

class BlockedNumberResponse(BlockedNumberBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Report Schemas
class ReportCreate(BaseModel):
    phone_number: str
    threat_type: Optional[str] = "رسالة نصية (SMS)"
    report_reason: str

class ReportResponse(BaseModel):
    id: int
    phone_number: str
    threat_type: str
    report_reason: str
    status: str
    reports_count: int = 1
    created_at: datetime

    class Config:
        from_attributes = True
