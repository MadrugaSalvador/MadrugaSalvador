from flask import Blueprint, render_template

relatorios_bp = Blueprint('relatorios', __name__)

@relatorios_bp.route('/')
def show_relatorios():
    return render_template('relatorios.html')
