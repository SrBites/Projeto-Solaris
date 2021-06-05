from flask import Flask, render_template, request
from modelagem_de_negocios.util import pathing
from modelagem_de_negocios.util import bd

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/cadastracliente', methods=['POST'])
def cadastraCliente():
    username = request.form['username']
    cep = int(request.form['cep'])
    password = request.form['senha']
    print('cheguei')

    mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
    print('cheguei 2')
    cmd = 'INSERT INTO tb_conta_cliente(nme_cliente,cep_cliente,senha_cliente) VALUES (%s, %s, %s;'
    mysql.executar(cmd, [username, cep, password])
    print('cheguei 3')
    return render_template('teste.html')


app.run()