from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort, get_flashed_messages
from app.autenticacion.autenticacion_bbdd import Usuario,RegistroUsuario, Login
from flask_login import login_user, logout_user, current_user, login_required
from app import login_manager, wraps
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

autenticacion = Blueprint('autenticacion', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        usu = str(current_user.rol)
        print(usu)
        if usu == 'normal':
            return redirect(url_for('autenticacion.login'))
        return f(*args, **kws)
    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@autenticacion.route('/', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        flash("No tienes permisos "+current_user.usuario)
        return redirect(url_for('panel.index'))

    form = Login(meta={'csrf':False})
    if form.validate_on_submit():
        usuario=Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usuario and usuario.check_password(form.password.data) and usuario.activo == True:
            #Si existe el usuario y el password y esta activo
            login_user(usuario)
            flash("Bienvenido de nuevo "+current_user.usuario)
            next = request.form['next']
            return redirect(next or url_for('panel.index'))
        else:
            flash("Usuario no existe", 'danger')
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('autenticacion/login.html', login=form)


@autenticacion.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('autenticacion.login'))

@autenticacion.route('/registro', methods = ('GET', 'POST'))
@login_required
@admin_required
def registro():
    if session.get('usuario'):
        print(session['username'])
    form = RegistroUsuario(meta={'csrf':False})
    if form.validate_on_submit():
        usuario = Usuario(form.usuario.data, form.apellido_uno.data, form.apellido_dos.data, form.password.data, form.rol.data, form.correo.data)
        db.session.add(usuario)
        db.session.commit()
        flash("Usuario creado con éxito")
        return redirect(url_for('autenticacion.registro'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('/autenticacion/registro.html', registro=form)