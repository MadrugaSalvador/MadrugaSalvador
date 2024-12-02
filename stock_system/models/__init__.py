import pymysql
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def conectar_no_banco():
    try:
        connection = pymysql.connect(
            host='db-erp.cx8ii00mwk8z.us-east-2.rds.amazonaws.com',
            user='madruguinha',
            password='CbP&dro123',
            db='erp_bd',
            port=3306
        )
        return connection
    except pymysql.MySQLError as err:
        print(f"Database Error: {err}")
        return None

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://madruguinha:CbP&dro123@db-erp.cx8ii00mwk8z.us-east-2.rds.amazonaws.com/erp_bd'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def get_inventario():
    connection = conectar_no_banco()
    produtos = []
    if connection:
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM inventario")
                produtos = cursor.fetchall()
        finally:
            connection.close()
    return produtos
