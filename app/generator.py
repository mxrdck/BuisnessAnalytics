#DROP ALL TABLES BEFORE RUNNING!

from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db
import names
import random

def add_patients():
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


#hp generator
def add_params():
    denotations = ["Blutzucker","Blutdruck","Eisen","Magnesium","Puls","Alkoholgehalt","THC"]

    for den in denotations:
        hp = HealthParameter(denotation=den)
        try:
            session.add(hp)
            session.commit()
        except:
            next


#add some values to random patients
#list of patients, parameters
def add_values():
    patients = session.query(Patient).all()
    parameters = session.query(HealthParameter).all()

    for patient in patients:
        for healthparam in parameters:

            #create value for param and add to db
            hv = HealthValue(value=random.randint(0, 100))
            healthparam.values.append(hv)
            ph = PatientHealth()
            ph.health_value = hv
            session.add(ph)
            patient.health_values.append(ph)
            session.commit()


if __name__ == '__main__':
    add_patients()
    add_params()
    add_values()

