from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime


db_string = "postgresql://postgres:1234@localhost:5432/patientdb"

db = create_engine(db_string)
base = declarative_base()

# many to many relationship for patient -> healthvalues

patienthealth = Table("patient_health",
                      base.metadata,
                      Column('patient_id', Integer,
                             ForeignKey('Patient.patient_nr')),
                      Column('healthvalue_id', Integer,
                             ForeignKey('HealthValue.gid')),
                      Column('date', DateTime, default=datetime.utcnow))


class Patient(base):
    __tablename__ = 'Patient'

    patient_nr = Column(Integer, primary_key=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    first_name = Column(String(256))
    last_name = Column(String(256), nullable=False)
    sex = Column(String, nullable=False)
    patient_health = relationship('HealthValue',
                                  secondary=patienthealth, backref='patient', lazy='dynamic')

    def __repr__(self):
        return '<Patient {}: {} {}>'.format(self.patient_nr, self.first_name, self.last_name)

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


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)