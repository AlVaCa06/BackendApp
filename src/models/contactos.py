

from flask import Flask, jsonify, request

from src.entities.entity import Session, engine, Base
from src.entities.contactos import Contacto, ContactosSchema
from datetime import datetime


def cargaContactos():
    session = Session()
    contactos_objects = session.query(Contacto).all()
    schema = ContactosSchema(many=True)
    contactos = schema.dump(contactos_objects)
    session.close()
    return jsonify(contactos)


def cargaContacto(json_contacto):
    try:
        id = json_contacto['id']
    except():
        id=0
    session = Session()
    contacto_objects = session.query(Contacto).filter(Contacto.id==id)
    schema = ContactosSchema(many=True)
    contacto = schema.dump(contacto_objects)
    session.close()
    return jsonify(contacto)

def guardaContacto(json_contacto):
    id= 0
    try:
        id = json_contacto['id']
        nombre = json_contacto['nombre']
        telefono = json_contacto['telefono']
        correo = json_contacto['correo']
        fechacumple = datetime.now()
        anios = json_contacto['anios']
        anios= int(anios)
    except():
        pass
    newcontacto = Contacto(nombre = nombre,
            telefono= telefono,
            correo = correo,
            fechacumple = datetime.now(),
            anios = anios)
    if(id > 0):
        session = Session()
        users_objects = session.query(Contacto).filter(Contacto.id==id).first()
        users_objects.nombre= nombre
        users_objects.telefono= telefono
        users_objects.correo= correo
        users_objects.anios= anios
        schema = ContactosSchema()
        contact = schema.dump(users_objects)
        session.commit()
        session.close()
    else:
        session = Session()
        session.add(newcontacto)
        session.flush()
        users_objects = newcontacto
        schema = ContactosSchema()
        contact = schema.dump(users_objects)
        session.commit()
        session.close()

    return jsonify(contact), 201
