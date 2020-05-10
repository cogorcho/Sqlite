from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#def init(db):
#    print(__name__,'init')
#    db = db

class Provincia(db.Model):
    def __init__(self, db):
        db = db

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Provincia %r %r>' % (self.id, self.nombre)

class Ambito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), unique=True, nullable=False)
    escuelas = db.relationship('Escuela', backref='ambito', lazy=True)

    def __repr__(self):
        return '<Ambito %r %r>' % (self.id, self.nombre)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), unique=True, nullable=False)
    escuelas = db.relationship('Escuela', backref='sector', lazy=True)

    def __repr__(self):
        return '<Sector %r %r>' % (self.id, self.nombre)

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProvincia = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    localidades = db.relationship('Localidad', backref='departamento', lazy=True)

    def __repr__(self):
        return '<Departamento %r %r %r>' % (self.id, self.idProvincia, self.nombre)

class Localidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    codigo = db.Column(db.String(32), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    escuelas = db.relationship('Escuela', backref='localidad', lazy=True)

    def __repr__(self):
        return '<Localidad %r %r %r %r %r>' % (self.id, self.idDepartamento, self.codigo, self.nombre, self.nombre)

class Escuela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idLocalidad  = db.Column(db.Integer, db.ForeignKey('localidad.id'), nullable=False)
    idSector  = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    idAmbito  = db.Column(db.Integer, db.ForeignKey('ambito.id'), nullable=False)
    codigo = db.Column(db.String(32), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    domicilio = db.Column(db.String(256), nullable=False)
    codpos = db.Column(db.String(64))
    tiposniveles = db.relationship('TedNivEscuela', backref='escuela', lazy=True)

    def __repr__(self):
        return '<Escuela %r %r %r %r %r %r %r %r>' % (self.id, self.idLocalidad, self.idSector, self.idAmbito, self.codigo, self.nombre, self.domicilio, self.codpos)

class NivelEducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    #niveleseducacion = db.relationship('TipoNivelEducacion', backref='niveleducacion', lazy=True)

    def __repr__(self):
        return '<NivelEducacion %r %r>' % (self.id, self.nombre)

class TipoEducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    #tiposeducacion = db.relationship('TipoNivelEducacion', backref='tipoeducacion', lazy=True)

    def __repr__(self):
        return '<TipoEducacion %r %r>' % (self.id, self.nombre)

class TipoNivelEducacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idTipoEducacion = db.Column(db.Integer, db.ForeignKey('tipoeducacion.id'), nullable=False)
    idNivelEducacion = db.Column(db.Integer, db.ForeignKey('niveleducacion.id'), nullable=False)
    #tiponiveleducacion = db.relationship('TipoNivelEducacion', backref='tiponiveleducacion', lazy=True)


    def __repr__(self):
        return '<TipoNivelEducacion %r %r>' % (self.id, self.nombre)

class TedNivEscuela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idEscuela = db.Column(db.Integer, db.ForeignKey('escuela.id'), nullable=False)
    idTipoNivel = db.Column(db.Integer, db.ForeignKey('tiponiveleducacion.id'), nullable=False)

    def __repr__(self):
        return '<TedNivEscuela %r %r %r>' % (self.id, self.idEscuela, self.idTipoNivel)


