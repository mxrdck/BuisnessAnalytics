from models import HealthValue, HealthParameter, Patient, patienthealth
from models import session, base, db




p = session.query(Patient).first()

print(p)

hv = session.query(HealthValue).first()

p.patient_health.append(hv)

session.commit()