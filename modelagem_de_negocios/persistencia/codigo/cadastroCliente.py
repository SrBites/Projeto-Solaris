from flask import Flask, request, render_template
from modelagem_de_negocios.util import bd
from modelagem_de_negocios.util import pathing

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/cadastracliente', methods='POST')
def cadastraCliente():
    username = request.form['username']
    cep = request.form['cep']
    password = request.form['senha']

    mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

    cmd = 'INSERT INTO conta_cliente VALUES (%s, %s, PASSWORD(%s));'
    mysql.executar(cmd, [username, cep, password])

    return render_template('teste.html', msg=msg)