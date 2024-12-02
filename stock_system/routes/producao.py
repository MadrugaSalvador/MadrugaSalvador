from flask import Blueprint, render_template

producao_bp = Blueprint('producao', __name__)

@producao_bp.route('/')
def show_producao():
    return render_template('producao.html')
