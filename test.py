from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from models.tablas import Provincia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Provincia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return "{'id': %r, 'nombre': %r}" % (self.id, self.nombre)

class Ambito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return "{'id': %r, 'nombre': %r}" % (self.id, self.nombre)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return "{'id': %r, 'nombre': %r}" % (self.id, self.nombre)

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProvincia = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "{'id': %r, 'idProvincia': %r, 'nombre': %r}" % (self.id, self.idProvincia, self.nombre)

class Localidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    codigo = db.Column(db.String(32), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "{'id': %r, 'idDepartamento': %r, 'codigo': %r, 'nombre': %r}" % (self.id, self.idDepartamento, self.codigo, self.nombre)

class Escuela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idLocalidad  = db.Column(db.Integer, db.ForeignKey('localidad.id'), nullable=False)
    idSector  = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    idAmbito  = db.Column(db.Integer, db.ForeignKey('ambito.id'), nullable=False)
    codigo = db.Column(db.String(32), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    domicilio = db.Column(db.String(256), nullable=False)
    codpos = db.Column(db.String(64))

    def __repr__(self):
        return "{'id': %r, 'idLocalidad': %r, 'idSector: %r, 'idAmbito: %r, 'codigo': %r, 'nombre': %r, 'domicilio': %r, 'codpos': %r}" %         (self.id, self.idLocalidad, self.idSector, self.idAmbito, self.codigo, self.nombre, self.domicilio, self.codpos)

class Niveleducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "{'id': %r, 'nombre': %r}" % (self.id, self.nombre)

class Tipoeducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    
    def __repr__(self):
        return "{'id': %r, 'nombre': %r}" % (self.id, self.nombre)

class Tiponiveleducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idTipoEducacion = db.Column(db.Integer, db.ForeignKey('tipoeducacion.id'), nullable=False)
    idNivelEducacion = db.Column(db.Integer, db.ForeignKey('niveleducacion.id'), nullable=False)

    def __repr__(self):
        return "{'id': %r, 'idTipoEducacion': %r, 'idNivelEducacion': %r}" % (self.id, self.idTipoEducacion, self.idNivelEducacion)

pcias = Provincia.query.all()
PCIAS = []
for d in pcias:
    PCIAS.append(d)

ambs = Ambito.query.all()
AMBITOS = []
for d in ambs:
    AMBITOS.append(d)

secs = Sector.query.all()
SECTORES = []
for d in secs:
    SECTORES.append(d)

deps = Departamento.query.filter(Departamento.idProvincia == 1).all()
DEPTOS = []
for d in deps:
    DEPTOS.append(d)

locs = Localidad.query.filter(Localidad.idDepartamento == 119).all()
LOCS = []
for d in locs:
    LOCS.append(d)

escs = Escuela.query.all()
ESCUELAS = []
for d in escs:
    ESCUELAS.append(d)

nives = Niveleducacion.query.all()
NIVELESE = []
for d in nives:
    NIVELESE.append(d)
    
tipos = Tipoeducacion.query.all()
TIPOSE = []
for d in tipos:
    TIPOSE.append(d)

tnes = Tiponiveleducacion.query.all()
TNES = []
for d in tnes:
    TNES.append(d)

#print(PCIAS)
#print(SECTORES)
#print(AMBITOS)
#print(DEPTOS)
print(LOCS)