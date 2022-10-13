from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, current_user
from functools import wraps
from flask_mysqldb import MySQL

app = Flask(__name__)
app.app_context().push()#RuntimeError: Working outside of application context.

# Esta parte para implementar panel
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'damian'
app.config['MYSQL_PASSWORD'] = 'Yvqvn1983-'
app.config['MYSQL_DB'] = 'panel'
mysql = MySQL(app)
#########################################


app.config.from_object('configuracion.ConfiguracionDesarrollo')
db = SQLAlchemy(app)

# LOGIN_FLASK
login_manager = LoginManager()  # Instancia de la clase LoginManager para flask_login
login_manager.init_app(app)  # Instacia de app
login_manager.login_view = "autenticacion.login"
login_manager.login_message = "No tienes permisos"

from .autenticacion.autenticacion_vista import autenticacion
from .panel.panel_vistas import panel
from .correos.correo_vistas import correo
from .backup.backup_vista import backup
from .documentacion.documentacion import documentacion

# VISTAS
app.register_blueprint(autenticacion)
app.register_blueprint(panel)
app.register_blueprint(correo)
app.register_blueprint(backup)
app.register_blueprint(documentacion)

db.create_all()
