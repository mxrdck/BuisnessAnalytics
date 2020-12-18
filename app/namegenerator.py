from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db
import names
import random
genders = ["male","female"]

for i in range(100):
    gender = genders[random.randint(0,1)]
    first_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()

    weight = round(random.uniform(40,180),2)
    height = round(random.uniform(1.5,2),2)

    sex = gender

    p = Patient(first_name=first_name,last_name=last_name, weight=weight, height=height, sex = gender)

    session.add(p)
    session.commit()


