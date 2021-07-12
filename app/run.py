from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from src.entities.entity import Session, engine, Base
from src.entities.contactos import Contactos, ContactosSchema
import src.models.contactos as contactos

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/cargacontactos')
def carga_contactos():
    return contactos.cargaContactos()

@app.route('/guardacontacto', methods=['post'])
def add_contacto():
    contacto = request.get_json()
    return contactos.guardaContacto(contacto)

@app.route('/getcontacto', methods=['post'])
def get_contacto():
    contacto = request.get_json()
    return contactos.cargaContacto(contacto)

if __name__ == '__main__':
    app.run( host='192.168.1.91', port=8080, debug=True)


