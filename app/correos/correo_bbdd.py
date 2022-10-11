from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import InputRequired, NumberRange
from decimal import Decimal

class Correos(db.Model):
    __tablename__ = 'copiamails'
    id = db.Column(db.Integer, primary_key = True)
    asunto = db.Column(db.Text(4294000000))
    contenido = db.Column(db.Text(4294000000))
    fecha_envio = db.Column(db.DateTime())
    fuente = db.Column(db.Text(4294000000))
    tipo_alerta = db.Column(db.Integer)


    def __init__(self, asunto, contenido, destino, fecha_envio, fuente, tipo_alerta):
        self.asunto = asunto
        self.contenido = contenido
        self.destino = destino
        self.fecha_envio = fecha_envio
        self.fuente = fuente
        self.tipo_alerta = tipo_alerta


    def __repr__(self):
        return 'Asunto %r'%(self.asunto)
'''
class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired()])
    precio = DecimalField('Precio', validators=[InputRequired(), NumberRange(min=Decimal('0.0'))])
'''