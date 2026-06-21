from database import SessionLocal
from models import SecurityLog, Incident

db = SessionLocal()

log = SecurityLog(
    event_type="failed_login",
    username="admin",
    ip_address="192.168.1.10",
    severity="High"
)

incident = Incident(
    threat="Brute Force Attack",
    severity="High",
    status="Open"
)

db.add(log)
db.add(incident)

db.commit()

print("Data inserted successfully!")