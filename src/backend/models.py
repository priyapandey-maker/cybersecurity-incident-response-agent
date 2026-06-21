from sqlalchemy import Column, Integer, String
from database import Base


class SecurityLog(Base):
    __tablename__ = "security_logs"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    username = Column(String)
    ip_address = Column(String)
    severity = Column(String, nullable=False)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    threat = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, default="Open")