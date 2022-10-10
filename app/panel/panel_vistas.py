from flask import Blueprint, render_template, request, url_for, flash, redirect, abort, session
from app.panel.panel_bbdd import RegistroServidor, Servidores, FormSINO
from app import db, mysql
#from app import db, mysql #msyql para implementar el buscador
from flask_login import login_required
from werkzeug.utils import secure_filename
import paramiko, re
from werkzeug.security import check_password_hash


panel = Blueprint('panel',__name__)


@panel.before_request
@login_required

def validacion():
    pass

@panel.route('/panel')
def index():
    servidor = Servidores.query.order_by(Servidores.nombre.asc())
    return render_template('/panel/index.html', listado=servidor)

#REGISTRO DE SERVIDORES
@panel.route('/panel/registro', methods = ('GET', 'POST'))
def registro():
    form = RegistroServidor(meta={'csrf':False})
    if form.validate_on_submit():
        servidor = Servidores(form.nombre.data, form.usuario.data, form.clave.data, form.ip.data)
        db.session.add(servidor)
        db.session.commit()
        flash("Servidor creado")
        return redirect(url_for('panel.index'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('panel/registro_servidor.html', servidor=form)

#DATOS DEL SERVIDOR SELECCIONADO
@panel.route('/panel/<int:id_servidor>', methods = ['GET', 'POST'])
def servidor(id_servidor):
    servidor = Servidores.query.get_or_404(id_servidor)

    #CONEXIÓN AL SERVIDOR
    host = servidor.ip
    usuario = servidor.usuario
    password = servidor.clave
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cliente.connect(host, username=usuario, password=password, allow_agent=False, look_for_keys=False)

    #COMANDO INFORMACIÓN DEL DISCO
    stdin, stdout, stderr = cliente.exec_command("df -h | sed -e 's/ \+/\t/g' ")#Expresión regular para sustituir los espacios por un tabulador
    salida = ((stdout.read()).decode('UTF-8').split('\n'))
    salidaFormateada = salida[1:-1]

    salidaFinal = []
    for particion in salidaFormateada:
        salidaAuxiliar = particion.split('\t')

        for elemento in salidaAuxiliar:
            if '/dev/sd' in elemento:#Para filtrar y sacar solo las lineas con /dev/sd
                salidaFinal.append(salidaAuxiliar)

    #COMANDO ESTADO DE RAM
    entrada, salidaram,error = cliente.exec_command("free -m | sed -e 's/ \+/\t/g' ")
    ram = ((salidaram.read()).decode('UTF-8').split('\n'))
    ram2 = ram[1:-1]
    ram3 = ram2[0]#Para obtener solo la fila de la RAM
    swat = ram2[1] #PARA OBTENER LA SWAT
    ramMem = []
    ramMem.append(ram3)
    for ram in ramMem:
        ramAuxiliar = ram.split('\t')

    ramSwat = []
    ramSwat.append(swat)
    for swat in ramSwat:
        swatAuxiliar = swat.split('\t')

    #COMANDO PROCESOS ABIERTOS
    stdin, stdout, stderr = cliente.exec_command(" ps aux | awk '{print $2, $3, $4, $11}' | sort -k2r | head -n 15 | sed -e 's/ \+/\t/g'")#Expresión regular para sustituir los espacios por un tabulador
    salida = ((stdout.read()).decode('UTF-8').split('\n'))
    salidaFormateada = salida[1:-1]

    ProcesoFinal = []
    for procesoAbierto in salidaFormateada:
        proceso = procesoAbierto.split('\t')
        ProcesoFinal.append(proceso)
    return render_template('panel/servidores.html', servidor=servidor, disco=salidaFinal, ram=ramAuxiliar, swat=swatAuxiliar ,usuario=usuario, id_servidor=id_servidor, procesos=ProcesoFinal)

#ELIMINAR SERVIDOR
@panel.route('/panel/eliminarServidor/<int:id_servidor>', methods = ['GET', 'POST'])
def eliminarServidor(id_servidor):
    servidor = Servidores.query.get_or_404(id_servidor)
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM servidores where id_servidor = {}'.format(id_servidor))
    if servidor is None:
        abort(404)
    formulario = FormSINO(meta={'csrf':False})
    if formulario.validate_on_submit():
        if formulario.si.data:
            cur=mysql.connection.cursor()
            cur.execute('DELETE backup FROM backup WHERE servidor_id = {}'.format(id_servidor))
            mysql.connection.commit()
            cur = mysql.connection.cursor()
            cur.execute('DELETE servidores FROM servidores WHERE id_servidor = {}'.format(id_servidor))
            mysql.connection.commit()
            flash("Servidor Eliminado")
        return redirect(url_for('panel.index', id_servidor=id_servidor))
    return render_template('panel/eliminarservidor.html',id_servidor=id_servidor, servidor=servidor, formularios=formulario)

