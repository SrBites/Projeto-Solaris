from flask import Flask, request
from modelagem_de_negocios.util import bd
from modelagem_de_negocios.util import pathing

mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/cadastrarCliente', methods='POST')
def cadastraCliente():
    username = request.form['username']
    cep = request.form['cep']
    password = request.form['senha']

    cmd = '''
    INSERT INTO conta_cliente VALUES (%s, %s, PASSWORD(%s));
    '''