from app import db
from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, SelectField, SubmitField, BooleanField
from wtforms.validators import InputRequired, EqualTo, Email
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {'extend_existing' : True}
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(255))
    apellido_uno = db.Column(db.String(255))
    apellido_dos = db.Column(db.String(255))
    password = db.Column(db.String(300))
    rol = db.Column(db.String(10))
    correo = db.Column(db.String(255))
    activo = db.Column(db.Boolean, default=True)
    fecha = db.Column (db.DateTime, default=datetime.now())

    @property
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def __init__(self, usuario,apellido_uno, apellido_dos, password, rol, correo):
        self.usuario = usuario
        self.apellido_uno = apellido_uno
        self.apellido_dos = apellido_dos
        self.password = generate_password_hash(password)
        self.rol = rol
        self.correo = correo

    def check_password(self, password):
        return check_password_hash(self.password, password)


#FORMULARIOS
class RegistroUsuario(FlaskForm):
    usuario = StringField('Usuario', validators=[InputRequired()])
    apellido_uno = StringField('Primer Apellido')
    apellido_dos = StringField('Segundo Apellido')
    password = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('confirmar')])
    confirmar = PasswordField('Repite la contraseña')
    rol = SelectField('Permisos', choices=[('normal', 'normal'), ('admin', 'admin')], validators=[InputRequired()])
    correo = StringField('correo')

class Login(FlaskForm):
    usuario = StringField('Nombre', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])
    next = HiddenField('next')