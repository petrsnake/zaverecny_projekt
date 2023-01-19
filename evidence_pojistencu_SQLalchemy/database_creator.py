# necessary imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# making engine
engine = create_engine('sqlite:///database_insurance.db', echo=False)

# base class for declaration of teble classes
Base = declarative_base(engine)

# Table of insurance
class Insurance(Base):
    __tablename__ = 'insurance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    telephone = Column(Integer, nullable=False)

    def __repr__(self):
        #Text representation
        return f'<ID: {self.id}, jmeno: {self.name} {self.lastname}, věk: {self.age}, tel: {self.telephone}>'

# making database
Base.metadata.create_all(engine)

# making session for work with data
Session = sessionmaker(bind=engine)
session = Session()


