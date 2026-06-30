from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session


from src.backend.database import engine, SessionLocal, Base
from src.backend.models import Incident


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cybersecurity Incident Response Agent API",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PhishingAlert(BaseModel):
    event_type: str
    sender: str
    subject: str
    attachment: Optional[str] = None
    severity: str

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "incident-response-backend"}


@app.post("/api/chat")
async def process_phishing_alert(alert: PhishingAlert, db: Session = Depends(get_db)):
    try:
  
        threat_description = f"Phishing attempt identified from sender: {alert.sender} with subject: '{alert.subject}'"
        
        
        new_incident = Incident(
            threat=threat_description,
            severity=alert.severity,
            status="open"  
        )
        
        
        db.add(new_incident)
        db.commit()
        db.refresh(new_incident)

        return {
            "status": "processed_and_saved",
            "incident_id": new_incident.id,
            "severity": new_incident.severity,
            "message": "Security telemetry successfully parsed and written to the system database ledger."
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database write failure: {str(e)}")
