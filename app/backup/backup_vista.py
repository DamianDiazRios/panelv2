from flask import Blueprint, render_template, request, url_for, flash, redirect, abort
from app import db, mysql
from app.backup.backup_bbdd import Backup, BackupFormulario ,FormSINO
from app.autenticacion.autenticacion_vista import admin_required
from flask_login import login_required
from flask_login import login_required
#from app import CKEditor
from werkzeug.utils import secure_filename

backup = Blueprint('backup', __name__)

@backup.before_request
@login_required
@admin_required

def validacion():
    pass

@backup.route('/backuplistado')
@backup.route('/backuplistado/<int:page>')
def backuplistado(page=1):
    backup = Backup.query.order_by(Backup.APLICACION.asc())
    return render_template('backup/backuplistado.html', listado = backup.paginate(page, 8))


@backup.route('/backupmostrar/<int:id>', methods=['GET', 'POST'])
def backupmostrar(id):
    backup=Backup.query.get({"id":id})
    return render_template('backup/backupmostrar.html', backup=backup)

@backup.route('/backup-nuevo', methods=('GET', 'POST'))
def nuevo():
    formulario = BackupFormulario(meta={'csrf':False})
    if formulario.validate_on_submit():
        b = Backup(request.form['APLICACION'], request.form['SERVIDOR_EJECUCION'], request.form['SERVIDOR_BACKUP_1'], request.form['PERIOCIDAD_1'], request.form['HORA_1'], request.form['TIPO_1'], request.form['RUTA_1'], request.form['SERVIDOR_BACKUP_2'], request.form['PERIOCIDAD_2'], request.form['HORA_2'], request.form['RUTA_2'], request.form['SERVIDOR_BACKUP_3'], request.form['PERIOCIDAD_3'], request.form['HORA_3'], request.form['RUTA_3'],request.form['SERVIDOR_BACKUP_4'], request.form['PERIOCIDAD_4'], request.form['HORA_4'], request.form['RUTA_4'], request.form['OBSERVACIONES'])
        db.session.add(b)
        db.session.commit()
        flash("Backup creado con éxito")
        return redirect(url_for('backup.backuplistado'))
    if formulario.errors:
        flash(formulario.errors, 'danger')
    return render_template('/backup/backupnuevo.html', formularios = formulario)

@backup.route('/backup-editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aplicacion = Backup.query.get_or_404(id)
    formulario = BackupFormulario(meta={'csrf':False})

    if request.method == 'GET':
        formulario.APLICACION.data = aplicacion.APLICACION
        formulario.SERVIDOR_EJECUCION.data = aplicacion.SERVIDOR_EJECUCION
        formulario.SERVIDOR_BACKUP_1.data = aplicacion.SERVIDOR_BACKUP_1
        formulario.PERIOCIDAD_1.data = aplicacion.PERIOCIDAD_1
        formulario.HORA_1.data = aplicacion.HORA_1
        formulario.TIPO_1.data = aplicacion.TIPO_1
        formulario.RUTA_1.data = aplicacion.RUTA_1
        formulario.SERVIDOR_BACKUP_2.data = aplicacion.SERVIDOR_BACKUP_2
        formulario.PERIOCIDAD_2.data = aplicacion.PERIOCIDAD_2
        formulario.HORA_2.data = aplicacion.HORA_2
        formulario.RUTA_2.data = aplicacion.RUTA_2
        formulario.SERVIDOR_BACKUP_3.data = aplicacion.SERVIDOR_BACKUP_3
        formulario.PERIOCIDAD_3.data = aplicacion.PERIOCIDAD_3
        formulario.HORA_3.data = aplicacion.HORA_3
        formulario.RUTA_3.data = aplicacion.RUTA_3
        formulario.SERVIDOR_BACKUP_4.data = aplicacion.SERVIDOR_BACKUP_4
        formulario.PERIOCIDAD_4.data = aplicacion.PERIOCIDAD_4
        formulario.HORA_4.data = aplicacion.HORA_4
        formulario.RUTA_4.data = aplicacion.RUTA_4
        formulario.OBSERVACIONES.data = aplicacion.OBSERVACIONES

    if formulario.validate_on_submit():
        aplicacion.APLICACION = formulario.APLICACION.data
        aplicacion.SERVIDOR_EJECUCION = formulario.SERVIDOR_EJECUCION.data
        aplicacion.SERVIDOR_BACKUP_1 = formulario.SERVIDOR_BACKUP_1.data
        aplicacion.PERIOCIDAD_1 = formulario.PERIOCIDAD_1.data
        aplicacion.HORA_1 = formulario.HORA_1.data
        aplicacion.TIPO_1 = formulario.TIPO_1.data
        aplicacion.RUTA_1 = formulario.RUTA_1.data
        aplicacion.SERVIDOR_BACKUP_2 = formulario.SERVIDOR_BACKUP_2.data
        aplicacion.PERIOCIDAD_2 = formulario.PERIOCIDAD_2.data
        aplicacion.HORA_2 = formulario.HORA_2.data
        aplicacion.RUTA_2 = formulario.RUTA_2.data
        aplicacion.SERVIDOR_BACKUP_3 = formulario.SERVIDOR_BACKUP_3.data
        aplicacion.PERIOCIDAD_3 = formulario.PERIOCIDAD_3.data
        aplicacion.HORA_3 = formulario.HORA_3.data
        aplicacion.RUTA_3 = formulario.RUTA_3.data
        aplicacion.SERVIDOR_BACKUP_4 = formulario.SERVIDOR_BACKUP_4.data
        aplicacion.PERIOCIDAD_4 = formulario.PERIOCIDAD_4.data
        aplicacion.HORA_4 = formulario.HORA_4.data
        aplicacion.RUTA_4 = formulario.RUTA_4.data
        aplicacion.OBSERVACIONES = formulario.OBSERVACIONES.data
        print(aplicacion.APLICACION)
        db.session.add(aplicacion)
        db.session.commit()
        flash("Producto actualizado")
        return redirect(url_for('backup.editar', id=aplicacion.id))

    if formulario.errors:
        flash(formulario.errors, 'danger')
    return render_template('/backup/backup-editar.html', aplicacion=aplicacion, formularios=formulario)

@backup.route('/backup-eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    backup = Backup.query.get_or_404(id)
    if backup is None:
        abort(404)
    formulario = FormSINO(meta={'csrf':False})
    if formulario.validate_on_submit():
        if formulario.si.data:
            db.session.delete(backup)
            db.session.commit()
        return redirect(url_for('backup.backuplistado'))
    return render_template("/backup/eliminar.html", backup=backup, formularios=formulario)