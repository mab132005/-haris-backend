from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class BlockedNumber(Base):
    __tablename__ = "blocked_numbers"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    reason = Column(String, nullable=False)
    severity = Column(String, default="خطر شديد")
    created_at = Column(DateTime, default=datetime.utcnow)

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True, nullable=False)
    threat_type = Column(String, default="رسالة نصية (SMS)")
    report_reason = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending, approved, rejected
    created_at = Column(DateTime, default=datetime.utcnow)
