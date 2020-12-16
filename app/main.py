from models import Patient, HealthValue, HealthParameter, patient_health
from models import session, base, db

db_string = "postgresql://postgres:1234@localhost:5432/patientdb"


base.metadata.create_all(db)

hv = HealthValue(parameter=1,value=20,patient=1)

session.add(hv)
session.commit()

