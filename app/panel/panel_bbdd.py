from app import db
from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, SelectField, SubmitField, BooleanField, DateField
from wtforms.validators import InputRequired, EqualTo, Email
from werkzeug.security import check_password_hash, generate_password_hash

class Servidores(db.Model):
    __tablename__ = 'servidores'
    __table_args__ = {'extend_existing': True}
    id_servidor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    usuario = db.Column(db.String(255))
    clave = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    bbdd = db.relationship('Backup', backref='servidores', lazy='select', cascade="all, delete")


    @property
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def __init__(self, nombre, usuario, clave, ip):
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.ip = ip

#FOMULARIOS REGISTRO SERVIDOR
class RegistroServidor(FlaskForm):
    nombre = StringField('Nombre Servidor', validators=[InputRequired()])
    usuario = StringField('Usuario Servidor', validators=[InputRequired()])
    clave = StringField('Contraseña Servidor', validators=[InputRequired()])
    ip = StringField('Ip del Servidor', validators=[InputRequired()])




#BACKUP
class Backup(db.Model):
    __tablename__='backup'
    __table_args__ = {'extend_existing': True}
    id_backup = db.Column(db.Integer, primary_key= True)
    servidorCopia = db.Column(db.String(80))
    ruta = db.Column(db.String(250))
    nombreCopia = db.Column(db.String(80))
    servidor_id = db.Column(db.Integer, db.ForeignKey('servidores.id_servidor'), nullable= False)

    def __init__(self, servidorCopia, ruta, nombreCopia, servidor_id):
        self.servidorCopia = servidorCopia
        self.ruta = ruta
        self.nombreCopia = nombreCopia
        self.servidor_id = servidor_id

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

#FOMULARIOS REGISTRO BACKUP
class RegistroBackup(FlaskForm):
    servidorCopia = StringField('Servidor de Origen', validators=[InputRequired()])
    nombreCopia = StringField('Servicio a copiar', validators=[InputRequired()])
    servidor_id = SelectField('Servidor Backup', coerce=int)
    ruta = StringField('Ruta Backup', validators=[InputRequired()])






class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')