from flask import Flask, request, render_template
from modelagem_de_negocios.util import bd
from modelagem_de_negocios.util import pathing

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

@app.route('/cadastracliente', methods=['POST'])
def cadastraCliente():
    username = str(request.form['username'])
    cep = int(request.form['cep'])
    password = str(request.form['senha'])
    print('cheguei')

    mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
    print('cheguei 2')
    cmd = 'INSERT INTO tb_conta_cliente(nme_cliente,cep_cliente,senha_cliente) VALUES (%s, %s, PASSWORD(%s));'
    mysql.executar(cmd, [username, cep, password])
    print('cheguei 3')
    return render_template('teste.html')

app.run()
