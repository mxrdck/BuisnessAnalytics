from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Float, Date, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import date


db_string = "postgresql://postgres:1234@localhost:5432/patientdb"

db = create_engine(db_string)
base = declarative_base()

# many to many relationship for patient -> healthvalues


class PatientHealth(base):
    __tablename__ = "patient_health"
    patient_id = Column(Integer, ForeignKey('Patient.id'), primary_key=True)
    healthvalue_id = Column(Integer, ForeignKey('HealthValue.id'), primary_key=True)
    date = Column(Date, default=date.today())
    patient = relationship('Patient',back_populates='health_values')
    health_value = relationship('HealthValue',back_populates='patients')

class Patient(base):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    first_name = Column(String(256))
    last_name = Column(String(256), nullable=False)
    sex = Column(String, nullable=False)
    health_values = relationship('PatientHealth', back_populates="patient", cascade="delete")
    

    def __repr__(self):
        return '<Patient {}: {} {}>'.format(self.patient_nr, self.first_name, self.last_name)


class HealthValue(base):
    __tablename__ = 'HealthValue'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    parameter = Column(Integer, ForeignKey('HealthParameter.id'))
    patients = relationship('PatientHealth', back_populates="health_value")


class HealthParameter(base):
    __tablename__ = 'HealthParameter'

    id = Column(Integer, primary_key=True)
    denotation = Column(String(256), nullable=False)
    values = relationship(
        'HealthValue',
        backref='HealthParameter',
        lazy='dynamic')


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
