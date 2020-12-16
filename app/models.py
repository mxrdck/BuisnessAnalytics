from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime, timezone


db_string = "postgresql://postgres:1234@localhost:5432/patientdb"

db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)


# many to many relationship for patient -> healthvalues
class PatientHealth(base):
    __tablename__ = 'PatientHealth'

    patientnr = Column(Integer, ForeignKey("Patient.patient_nr"), primary_key=True)
    healthvalue = Column(Integer, ForeignKey("HealthValue.gid"), primary_key=True)
    date = Column(DateTime, nullable=False)


class Patient(base):
    __tablename__ = 'Patient'

    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    first_name = Column(String(256))
    last_name = Column(String(256), nullable=False)
    patient_nr = Column(Integer, primary_key=True)
    sex = Column(String, nullable=False)


class HealthValue(base):
    __tablename__ = 'HealthValue'

    gid = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    parameter = Column(Integer, ForeignKey('HealthParameter.hpid'))


class HealthParameter(base):
    __tablename__ = 'HealthParameter'

    hpid = Column(Integer, primary_key=True)
    denotation = Column(String(256), nullable=False)
    values = relationship(
        'HealthValue',
        backref='HealthParameter',
        lazy='dynamic')
