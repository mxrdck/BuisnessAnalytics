from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db

db_string = "postgresql://postgres:1234@localhost:5432/patientdb"


base.metadata.create_all(db)

hp = HealthParameter(denotation="Hamidismus")

session.add(hp)
session.commit()

hv = HealthValue(value=30, parameter=1)

session.add(hv)
session.commit()

p = Patient(height=12, weight=1, first_name="Has", last_name="Mid", sex="gay")

session.add(p)
session.commit()

ph = PatientHealth(patientnr=1, healthvalue=1)

session.add(ph)
session.commit()
