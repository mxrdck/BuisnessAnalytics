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
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('Patient.id'))
    healthvalue_id = Column(Integer, ForeignKey('HealthValue.id'))
    date = Column(Date, default=date.today())
    patient = relationship('Patient',back_populates='health_values')
    health_value = relationship('HealthValue',back_populates='patients', cascade = "delete")


    def __repr__(self):
        return '{} {}'.format(self.healthvalue_id, self.health_value.__to_param_and_val__())

class Patient(base):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    sex = Column(String, nullable=False)
    health_values = relationship('PatientHealth', back_populates="patient", cascade="all, delete, delete-orphan")
    

    def __repr__(self):
        return '<Patient {}: {} {}>'.format(self.id, self.first_name, self.last_name)


class HealthValue(base):
    __tablename__ = 'HealthValue'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    parameter = Column(Integer, ForeignKey('HealthParameter.id'))
    patients = relationship('PatientHealth', back_populates="health_value", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return '{}: {} {}'.format(self.id, session.query(HealthParameter).filter_by(id=self.parameter).first().denotation, self.value)

    def __to_param_and_val__(self):
        return '{} = {}'.format(session.query(HealthParameter).filter_by(id=self.parameter).first().denotation, self.value)
class HealthParameter(base):
    __tablename__ = 'HealthParameter'

    id = Column(Integer, primary_key=True, autoincrement=True)
    denotation = Column(String(256), nullable=False, unique=True)
    values = relationship(
        'HealthValue',
        backref='HealthParameter',
        cascade="all,delete, delete-orphan, save-update")

    def __repr__(self):
        return '{}: {}'.format(self.id, self.denotation)

Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
