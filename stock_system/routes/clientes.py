from flask import Blueprint, render_template

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/')
def show_clientes():
    return render_template('clientes.html')
