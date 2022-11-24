from app import db
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, SubmitField
from wtforms.validators import InputRequired

class Backup(db.Model):
    __tablename__='backup'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    APLICACION = db.Column(db.String(50))
    SERVIDOR_EJECUCION = db.Column(db.String(50))
    SERVIDOR_BACKUP_1 = db.Column(db.String(50))
    PERIOCIDAD_1 = db.Column(db.String(3000))
    HORA_1 = db.Column(db.String(50))
    TIPO_1 = db.Column(db.String(50))
    RUTA_1 = db.Column(db.String(100))
    SERVIDOR_BACKUP_2 = db.Column(db.String(50))
    PERIOCIDAD_2 = db.Column(db.String(3000))
    HORA_2 = db.Column(db.String(50))
    RUTA_2 = db.Column(db.String(100))
    SERVIDOR_BACKUP_3 = db.Column(db.String(50))
    PERIOCIDAD_3 = db.Column(db.String(3000))
    HORA_3 = db.Column(db.String(50))
    RUTA_3 = db.Column(db.String(100))
    SERVIDOR_BACKUP_4 = db.Column(db.String(50))
    PERIOCIDAD_4 = db.Column(db.String(3000))
    HORA_4 = db.Column(db.String(50))
    RUTA_4 = db.Column(db.String(100))
    OBSERVACIONES = db.Column(db.String(500))


    def __init__(self, APLICACION=None, SERVIDOR_EJECUCION=None, SERVIDOR_BACKUP_1=None, PERIOCIDAD_1=None, HORA_1=None, TIPO_1=None, RUTA_1=None, SERVIDOR_BACKUP_2=None, PERIOCIDAD_2=None, HORA_2=None, RUTA_2=None, SERVIDOR_BACKUP_3=None, PERIOCIDAD_3=None, HORA_3=None, RUTA_3=None, SERVIDOR_BACKUP_4=None, PERIOCIDAD_4=None, HORA_4=None, RUTA_4=None, OBSERVACIONES=None):
        self.APLICACION = APLICACION
        self.SERVIDOR_EJECUCION = SERVIDOR_EJECUCION
        self.SERVIDOR_BACKUP_1 = SERVIDOR_BACKUP_1
        self.PERIOCIDAD_1 = PERIOCIDAD_1
        self.HORA_1 = HORA_1
        self.TIPO_1 = TIPO_1
        self.RUTA_1 = RUTA_1
        self.SERVIDOR_BACKUP_2 = SERVIDOR_BACKUP_2
        self.PERIOCIDAD_2 = PERIOCIDAD_2
        self.HORA_2 = HORA_2
        self.RUTA_2 = RUTA_2
        self.SERVIDOR_BACKUP_3 = SERVIDOR_BACKUP_3
        self.PERIOCIDAD_3 = PERIOCIDAD_3
        self.HORA_3 = HORA_3
        self.RUTA_3 = RUTA_3
        self.SERVIDOR_BACKUP_4 = SERVIDOR_BACKUP_4
        self.PERIOCIDAD_4 = PERIOCIDAD_4
        self.HORA_4 = HORA_4
        self.RUTA_4 = RUTA_4
        self.OBSERVACIONES = OBSERVACIONES


#CLASES FORMULARIO
class BackupFormulario(FlaskForm):
        APLICACION = StringField('Aplicación', validators=[InputRequired()])
        SERVIDOR_EJECUCION = StringField('Servidor en ejecución', default=None)
        SERVIDOR_BACKUP_1 = StringField('Servidor Backup 1')
        PERIOCIDAD_1 = TextAreaField('Periocidad Backup 1')
        HORA_1 = StringField('Hora Backup 1')
        TIPO_1 = SelectField('Tipo', choices=[("Base de datos", "Base de datos"), ("Código", "Codigo")])
        RUTA_1 = StringField('Ruta Backup 1')
        SERVIDOR_BACKUP_2 = StringField('Servidor Backup 2')
        PERIOCIDAD_2 = TextAreaField('Periocidad Backup 2')
        HORA_2 = StringField('Hora Backup 2')
        RUTA_2 = StringField('Ruta Backup 2')
        SERVIDOR_BACKUP_3 = StringField('Servidor Backup 3')
        PERIOCIDAD_3 = TextAreaField('Periocidad Backup 3')
        HORA_3 = StringField('Hora Backup 3')
        RUTA_3 = StringField('Ruta Backup 3')
        SERVIDOR_BACKUP_4 = StringField('Servidor Backup 4')
        PERIOCIDAD_4 = TextAreaField('Periocidad Backup 4')
        HORA_4 = StringField('Hora Backup 4')
        RUTA_4 = StringField('Ruta Backup 4')
        OBSERVACIONES = TextAreaField('Observaciones: ')
class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')
