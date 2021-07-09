

from flask import Flask, jsonify, request

from src.entities.entity import Session, engine, Base
from src.entities.contactos import Contacto, ContactosSchema


def cargaContactos():
    session = Session()
    contactos_objects = session.query(Contacto).all()
    schema = ContactosSchema(many=True)
    contactos = schema.dump(contactos_objects)
    session.close()
    return jsonify(contactos)
