from flask import Flask, render_template
from stock_system.models import init_app, db
from routes.inventory import inventory_bp

app = Flask(__name__)
init_app(app)

# Registrando os Blueprints
app.register_blueprint(inventory_bp, url_prefix='/inventory')

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criação de tabelas
    app.run(debug=True)
