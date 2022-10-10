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





class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')