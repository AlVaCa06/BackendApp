from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

engine = create_engine ('postgresql://postgres:valles666@localhost:5432/Agenda')


Session = sessionmaker(bind=engine)

Base = declarative_base()
class Contactos():
    id = Column(Integer, primary_key = True )
    def __init__(self):
        self

