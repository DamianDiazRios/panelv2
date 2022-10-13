from flask import Blueprint, render_template, request
from app import mysql

#from app import db, mysql #msyql para implementar el buscador
from flask_login import login_required


correo = Blueprint('correo',__name__)


@correo.before_request
@login_required

def validacion():
    pass

@correo.route('/correo')
def copiamails():

    cur = mysql.connection.cursor()
    cur.execute("SELECT YEAR(fecha_envio) from copiamails group by YEAR(fecha_envio) ORDER BY fecha_envio desc")
    datos = cur.fetchall()
    aniosum = []
    anios = list(datos)
    for anio in anios:
        anio = (anio[0])
        aniosum.append(anio)
    return render_template('correo/correolistado.html', anios = aniosum)


@correo.route('/correos/<anio>')
def copiamailsAnio(anio):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, asunto, fecha_envio, fuente FROM copiamails WHERE YEAR(fecha_envio) ='{}' ORDER BY fecha_envio DESC".format(anio))
    anios = cur.fetchall()
    anios = list(anios)
    return render_template('correo/copiamails.html', mails = anios, anio=anio)

@correo.route('/correo/<int:id>')
def correos(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, asunto, contenido, destino, fecha_envio, fuente, tipo_alerta FROM copiamails WHERE id ='{}'".format(id))
    correoCompleto = cur.fetchall()
    correoCompleto = list(correoCompleto)
    for elemento in correoCompleto:
        correos = elemento[3].split(';')
        correos = correos[:-1]
        correos =", ".join(correos)
        print(correos)
    return render_template('correo/correoCompleto.html', correo = correoCompleto, correos = correos)

@correo.route('/correo/buscar', methods=['POST'])
def buscar():
    if request.method == 'POST':
        asunto = request.form['asunto']
        print(asunto)
        cur = mysql.connection.cursor()
        asunto = f"%{asunto}%"
        cur.execute("SELECT id, asunto, contenido, destino, fecha_envio, fuente, tipo_alerta FROM copiamails WHERE asunto like %s ORDER BY fecha_envio DESC", {asunto})
        asunto = cur.fetchall()
        print(asunto)
        return render_template("correo/buscador.html", asuntos=asunto)