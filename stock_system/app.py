from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from models import init_app, db, get_inventario
from routes.inventory import inventory_bp
from routes.producao import producao_bp
from routes.clientes import clientes_bp
from routes.fornecedores import fornecedores_bp
from routes.relatorios import relatorios_bp

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
init_app(app)

# Registrando os Blueprints
app.register_blueprint(inventory_bp, url_prefix='/inventory')
app.register_blueprint(producao_bp, url_prefix='/producao')
app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(fornecedores_bp, url_prefix='/fornecedores')
app.register_blueprint(relatorios_bp, url_prefix='/relatorios')

@app.route('/')
def index():
    if 'username' in session:
        return render_template('base.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Login inválido!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/api/inventario')
def api_inventario():
    produtos = get_inventario()
    return jsonify(produtos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criação de tabelas
    app.run(debug=True)
