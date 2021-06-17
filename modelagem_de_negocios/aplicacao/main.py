from flask import Flask, render_template, session, flash, url_for, redirect
from modelagem_de_negocios.persistencia.codigo import cadastro, login
from modelagem_de_negocios.util import pathing

'''
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=modelagem_de_negocios.aplicacao.main.py
flask run
'''

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())
app.secret_key = 'ventodonorte'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Voce deve estar logado para acessar esta função')
        return render_template('login.html')
    return render_template('quemsomos.html')

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
    flash('Cliente cadastrada com sucesso!')
    return render_template('login.html')


@app.route('/cadastraempresa', methods=['POST'])
def cadastraEmpresa():
    cad_e = cadastro.ContaEmpresa()
    cad_e.cadastra()
    flash('Empresa cadastrada com sucesso!')
    return render_template('login.html')

@app.route('/logincliente', methods=['POST'])
def loginCliente():
    log_c = login.LoginCliente()
    if log_c.loga():
        session['usuario_logado'] = log_c.getDados(0)
        usuario = log_c.getDados(1)
        flash(f'Olá, {usuario}! Login efetuado com sucesso!')
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/loginempresa', methods=['POST'])
def loginEmpresa():
    log_e = login.LoginEmpresa()
    if log_e.loga():
        return render_template('index.html')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado, faça o login novamente para ter acesso a todas funcionalidades do site')
    return render_template('index.html')

app.run()