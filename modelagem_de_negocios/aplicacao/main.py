from flask import Flask, render_template
<<<<<<< HEAD
from modelagem_de_negocios.persistencia.codigo import cadastro#, login
=======
from modelagem_de_negocios.persistencia.codigo import cadastro, login
>>>>>>> 3020bcd519d8e798a1af6f3b00ff6975a2b3c558
from modelagem_de_negocios.util import pathing

'''
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=modelagem_de_negocios.aplicacao.main.py
flask run
'''

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/login')
def formLogin():
    return render_template('login.html')

@app.route('/cadastro')
def formCadastro():
    return render_template('cadastro.html')

'''
@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')
'''

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


@app.route('/logincliente', methods=['POST'])
def loginCliente():
    log_c = login.ContaCliente()
    if log_c.loga():
        return render_template('index.html')
    else:
        return render_template('login.html')

'''
@app.route('/loginempresa', methods=['POST'])
def loginEmpresa():
    log_e = login.ContaEmpresa()
    log_e.loga()
    return render_template('index.html')
'''
app.run()