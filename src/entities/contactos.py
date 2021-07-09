from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Date
from .entity import Contactos, Base

class ContactosSchema(Schema):
    id = fields.Number()
    nombre=fields.Str()
    telefono=fields.Str()
    correo=fields.Str()
    fechacumple =  fields.Date()
    anios= fields.Str()

class Contacto(Contactos, Base):
    __tablename__ = 'contactos'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    nombre= Column(String)
    telefono= Column(String)
    correo= Column(String)
    fechacumple= Column(Date)
    anios= Column(String)

    def __init__(self, nombre, telefono, correo, fechacumple, anios):
        self.nombre = nombre
        self.telefono= telefono
        self.correo= correo
        self.fechacumple= fechacumple
        self.anios= anios



