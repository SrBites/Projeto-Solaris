from flask import Flask, request, render_template
from modelagem_de_negocios.persistencia.codigo import cadastro
from modelagem_de_negocios.util import pathing

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def formLogin():
    return render_template('login.html')

@app.route('/cadastro')
def formCadastro():
    return render_template('cadastro.html')

@app.route('/cadastracliente', methods=['POST'])
def cadastraCliente():
    cc = cadastro.ContaCliente()
    cc.cadastra()

    return render_template('index.html')

@app.route('/cadastraempresa', methods=['POST'])
def cadastraEmpresa():
    ce = cadastro.ContaEmpresa()
    ce.cadastra()

    return render_template('index.html')

app.run()