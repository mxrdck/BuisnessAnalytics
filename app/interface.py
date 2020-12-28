from models import HealthValue, HealthParameter, Patient, PatientHealth
from models import session, base, db
from sqlalchemy import exc 
class Interface:
    """
    Data Interface to handle database operations.

    """
    def __init__(self):
        '''what should happen here?'''
        pass

    # Basic CD: Patient, HealthParameter, HealthValue, PatientHealth
    # gui needs only create and delete operations for all tables and relations
    # patients are always queried by id


    # patients

    def add_patient(self, fname, lname, height, weight, sex):
        #TODO: are duplicate names allowed?
        from models import HealthValue, HealthParameter, Patient, PatientHealth
        from models import session, base, db
        p = Patient(first_name=fname, last_name=lname,
                    height=height, weight=weight, sex=sex)

        try:
            session.add(p)
            session.commit()
            return "Patient {} {} added.".format(p.first_name, p.last_name)
        except Exception as e:
            return str(e)


    def delete_patient(self,id=None):
        try:
            p = session.query(Patient).filter_by(id=id).first()
        except:
            return "Could not find patient in database."
        
        if p:
            try:
                session.delete(p)
                session.commit()
                return "Patient {} deleted".format(id)
            except Exception as e:
                return str(e)
        else:
            return "No Patient found with ID {}.".format(id)

    #TODO: add param, delete param, add value, delete value, add value to patient, add value to param, remove value from patient, remove value from param

    def add_health_param(self,denotation):
        ''' method to add health param to database
            duplicate params are not allowed
        '''
        hp = HealthParameter(denotation=denotation)
        try:
            session.add(hp)
            session.commit()
            return "Parameter {} added.".format(denotation)
        except exc.IntegrityError as e:
            return "Health Parameter '{}' already exists".format(denotation)

    def delete_health_param(self, id=None):
        try:
            hp = session.query(HealthParameter).filter_by(id=id).first()
        except:
            return "Could not find Parameter in database."
        
        if hp:
            try:
                session.delete(hp)
                session.commit()
                return "Health Parameter '{}' deleted".format(id)
            except Exception as e:
                return str(e)
        else:
            return "No Health Parameter found with ID {}.".format(id)


    def add_value_to_patient(self, patient_id, parameter_id, hv_date, hv_value):
        #TODO: try catch 
        try:
            p=session.query(Patient).filter_by(id=patient_id).first()
        except:
            return "No Patient with ID {} found.".format(patient_id)

        if p:
            hp = session.query(HealthParameter).filter_by(id=parameter_id).first()

            hv = HealthValue(value=hv_value)
            hp.values.append(hv)

            ph = PatientHealth(date=hv_date)
            #session.add(ph)
            ph.health_value = hv
            p.health_values.append(ph)

            session.commit()
            return "HV added to Patient"

        else:
            return "No Patient with ID {} found".format(patient_id)


    def remove_value_from_patient(self, patient_id, hv_id):
        #TODO: try catch 
        hv = session.query(HealthValue).filter_by(id=hv_id)
        session.delete(hv)
        session.commit()