from flask import Blueprint, render_template, request
from flask_login import login_required
from app.autenticacion.autenticacion_vista import admin_required

documentacion = Blueprint('documentacion',__name__)

@documentacion.before_request
@login_required

def validacion():
    pass

@documentacion.route('/documentacion/documentacion-formacion')
def DocumentacionFormacion():
    return render_template('/documentacion/documento-formacion.html')

@admin_required
def validacion():
    pass
@documentacion.route('/documentacion')
def indice():
    return render_template('documentacion/listado.html')

@documentacion.route('/documentacion/CambioContrasena')
def CambioContrasena():
    return render_template('documentacion/Cambio-contraseña-correo-ffis-imib.html')

@documentacion.route('/documentacion/Manual-conectar-unidad-de-red')
def ManualUnidadRed():
    return render_template('/documentacion/Manual-conectar-unidad-de-red.html')

@documentacion.route('/documentacion/documento-servidores')
def DocumentoServidores():
    return render_template('/documentacion/documento-servidores.html')

