from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db
import datetime

db_string = "postgresql://postgres:1234@localhost:5432/patientdb"


base.metadata.create_all(db)

hp = HealthParameter(denotation="Hamidismus")
session.add(hp)
hp = HealthParameter(denotation="Plebismus")
session.add(hp)
hp = HealthParameter(denotation="Maxismus")
session.add(hp)
session.commit()

hv = HealthValue(value=30, parameter=1)
session.add(hv)
hv = HealthValue(value=20, parameter=1)
session.add(hv)
hv = HealthValue(value=10, parameter=1)
session.add(hv)
hv = HealthValue(value=5, parameter=2)
session.add(hv)
hv = HealthValue(value=2, parameter=2)
session.add(hv)
session.commit()

p = Patient(height=120, weight=120, first_name="Max", last_name="Kodeck", sex="male")
session.add(p)
p = Patient(height=160, weight=20, first_name="Theo", last_name="Frey", sex="female")
session.add(p)
p = Patient(height=147, weight=90, first_name="Fabian", last_name="Erlenbusch", sex="male")
session.add(p)
session.commit()

ph = PatientHealth(patientnr=1, healthvalue=1, date=datetime.datetime.now())
session.add(ph)
ph = PatientHealth(patientnr=1, healthvalue=2, date=datetime.datetime.now())
session.add(ph)

ph = PatientHealth(patientnr=2, healthvalue=2, date=datetime.datetime.now())
session.add(ph)
ph = PatientHealth(patientnr=2, healthvalue=3, date=datetime.datetime.now())
session.add(ph)
ph = PatientHealth(patientnr=2, healthvalue=4, date=datetime.datetime.now())
session.add(ph)
ph = PatientHealth(patientnr=2, healthvalue=5, date=datetime.datetime.now())
session.add(ph)

ph = PatientHealth(patientnr=3, healthvalue=2, date=datetime.datetime.now())
session.add(ph)
session.commit()
