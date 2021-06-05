from flask import Flask, render_template
from modelagem_de_negocios.persistencia.codigo import cadastro#, login
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
    cad_c = cadastro.ContaCliente()
    cad_c.cadastra()
    return render_template('login.html')

@app.route('/cadastraempresa', methods=['POST'])
def cadastraEmpresa():
    cad_e = cadastro.ContaEmpresa()
    cad_e.cadastra()
    return render_template('login.html')

'''
@app.route('/logincliente', methods=['POST'])
def loginCliente():
    log_c = login.ContaCliente()
    log_c.loga()
    return render_template('index.html')

@app.route('/loginempresa', methods=['POST'])
def loginEmpresa():
    log_e = login.ContaEmpresa()
    log_e.loga()
    return render_template('index.html')
'''
app.run()