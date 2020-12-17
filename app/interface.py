class Interface:
    """
    Data Interface to handle database operations.

    """
    from models import HealthValue, HealthParameter, Patient, PatientHealth
    from models import session, base, db

    def __init__(self):
        '''what should happen here?'''
        pass

    # Basic CRUD: Patient, HealthParameter, HealthValue, PatientHealth

    # patients

    def add_patient(self, fname, lname, height, weight, sex):
        p = Patient(first_name=fname, last_name=lname,
                    height=height, weight=weight, sex=sex)

        try:
            session.add(p)
            session.commit()
            return "Patient added."
        except Exception as e:
            return str(e)


    def delete_patient(self, fname, lname, height, weight, sex, id=None):
        try:
            if id:
                p = session.query(Patient).filter_by(id=id).first()
            else:
                p = session.query(Patient).filter_by(first_name=fname, last_name=lname).first()
        except:
            return "Could not find patient in database."
        
        try:
            session.delete(p)
            session.commit()
            return "Patient deleted"
        except Exception as e:
            return str(e)

    def update_patient(self, fname, lname, height, weight, sex, id=None):
        try:
            if id:
                p = session.query(Patient).filter_by(id=id).first()
            else:
                p = session.query(Patient).filter_by(first_name=fname, last_name=lname).first()
        except:
            return "Could not find patient in database."

    