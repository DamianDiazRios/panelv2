from flask import Blueprint, render_template, request, url_for, flash, redirect, abort
from app import db, mysql

from flask_login import login_required
from flask_login import login_required
#from app import CKEditor
from werkzeug.utils import secure_filename

backup = Blueprint('backup', __name__)

@backup.before_request
@login_required

def validacion():
    pass

@backup.route('/backuplistado')

def backuplistado():
    return "Backup"