from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db


#create patient, healthparam and add to db
'''p = Patient(height=2,weight=60, first_name="Tom",last_name="Riddle",sex="male")
hp = HealthParameter(denotation="Blutzucker")
session.add(p)
session.add(hp)

#create a healthvaluev for a healthparam
hv = HealthValue(value=22)
hp.values.append(hv)
session.commit()'''

#map hv tp patient
'''hv = session.query(HealthValue).first()
print(hv)
p = session.query(Patient).first()
print(p)
#ph constructur is empty bc date has a default
ph = PatientHealth()
print(ph)
ph.health_value = hv
session.commit()
p.health_values.append(ph)

session.commit()'''


#try do delete patient--> what happens to relation table? 
#works if model has "cascade=delete"
'''p = session.query(Patient).first()
session.delete(p)
session.commit()'''