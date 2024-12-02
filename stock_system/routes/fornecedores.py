from flask import Blueprint, render_template

fornecedores_bp = Blueprint('fornecedores', __name__)

@fornecedores_bp.route('/')
def show_fornecedores():
    return render_template('fornecedores.html')
