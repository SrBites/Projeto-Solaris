from flask import Flask, request, render_template
from modelagem_de_negocios.util import bd
from modelagem_de_negocios.util import pathing

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/cadastraempresa', methods='POST')
def cadastraEmpresa():
    nome_empresa = request.form['nome_empresa']
    cnpj = request.form['cnpj']
    atuacao = request.form['atuacao']
    link_empresa = request.form['link']
    password = request.form['senha']

    mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

    cmd = 'INSERT INTO conta_cliente VALUES (%s, %s, %s, %s, PASSWORD(%s));'
    mysql.executar(cmd, [nome_empresa, cnpj, atuacao, link_empresa, password])

    return render_template('teste.html', msg=msg)