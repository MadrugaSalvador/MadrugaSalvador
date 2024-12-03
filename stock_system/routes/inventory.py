from flask import Blueprint, render_template, request, redirect, url_for
from models import conectar_no_banco

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/')
def show_inventory():
    connection = conectar_no_banco()
    produtos = []
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM inventario")
                produtos = cursor.fetchall()
        finally:
            connection.close()
    return render_template('inventory.html', produtos=produtos)

@inventory_bp.route('/add_item', methods=['POST'])
def add_item():
    connection = conectar_no_banco()
    if connection:
        try:
            pn = request.form['pn']
            nome_produto = request.form['nome_produto']
            modelo = request.form['modelo']
            grupo_do_produto = request.form['grupo_do_produto']
            ncm = request.form['ncm']
            estoque_min = request.form['estoque_min']
            estoque_max = request.form['estoque_max']
            qtd_em_estoque = request.form['qtd_em_estoque']
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO inventario (PN, nome_produto, modelo, grupo_do_produto, NCM, estoque_min, estoque_max, Qtd_em_estoque)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (pn, nome_produto, modelo, grupo_do_produto, ncm, estoque_min, estoque_max, qtd_em_estoque))
                connection.commit()
        finally:
            connection.close()
    return redirect(url_for('inventory.show_inventory'))

@inventory_bp.route('/add_entrada', methods=['POST'])
def add_entrada():
    connection = conectar_no_banco()
    if connection:
        try:
            produto_id = request.form['produto_id']
            quantidade = request.form['quantidade']
            data_entrada = request.form['data_entrada']
            nfe = request.form['nfe']
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO entrada_estoque (produto_id, quantidade, data_entrada, nfe)
                    VALUES (%s, %s, %s, %s)
                """, (produto_id, quantidade, data_entrada, nfe))
                connection.commit()
        finally:
            connection.close()
    return redirect(url_for('inventory.show_inventory'))

@inventory_bp.route('/add_saida', methods=['POST'])
def add_saida():
    connection = conectar_no_banco()
    if connection:
        try:
            produto_id = request.form['produto_id_saida']
            quantidade = request.form['quantidade_saida']
            data_saida = request.form['data_saida']
            cliente = request.form['cliente']
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO saida_estoque (produto_id, quantidade, data_saida, cliente)
                    VALUES (%s, %s, %s, %s)
                """, (produto_id, quantidade, data_saida, cliente))
                connection.commit()
        finally:
            connection.close()
    return redirect(url_for('inventory.show_inventory'))
