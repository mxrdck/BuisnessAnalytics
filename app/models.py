from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime,timezone


db_string = "postgresql://postgres:1234@localhost:5432/patientdb"

db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)


#many to many relationship for patient -> healthvalues

patient_health = Table('patienthealth',base.metadata,Column("patient_id",Integer, ForeignKey("Patient.patient_nr")), Column("healthvalue_id",Integer,ForeignKey("healthvalue.gid")))

class Patient(base):  
    __tablename__ = 'Patient'
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    first_name = Column(String(256))
    last_name = Column(String(256), nullable=False)
    patient_nr = Column(Integer, primary_key=True)
    sex = Column(String, nullable=False)
    healthvalue = relationship(
        "HealthValue",
        secondary=patient_health,
        back_populates="patient")

class HealthValue(base):
    __tablename__ = 'healthvalue'
    gid = Column(Integer,primary_key=True)
    value = Column(Integer, nullable=False)
    parameter = Column(Integer, ForeignKey('healthparameter.hpid'))
    patient = relationship(
        "Patient",
        secondary=patient_health,
        back_populates="healthvalue")
    #TODO: one to many relationship 


class HealthParameter(base):
    __tablename__ = 'healthparameter'
    hpid = Column(Integer, primary_key=True)
    denotation = Column(String(256),nullable=False)
    values = relationship('HealthValue', backref='healthparameter', lazy='dynamic')