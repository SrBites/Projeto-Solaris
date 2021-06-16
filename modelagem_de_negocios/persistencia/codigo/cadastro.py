from flask import request
from modelagem_de_negocios.util import bd

class ContaCliente:
    def cadastra(self):
        username = request.form['username']
        password = request.form['senha']
        cep = int(request.form['cep'])

        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
        cmd = 'INSERT INTO tb_conta_cliente(nme_cliente, senha_cliente, cep_cliente) VALUES (%s, %s, %s);'

        mysql.executar(cmd, [username, password, cep])

class ContaEmpresa:
    def cadastra(self):
        nme_empresa = request.form['nome_empresa']
        cnpj = request.form['cnpj']
        reg_atuacao = request.form['atuacao']
        password = request.form['senha']
        url = request.form['link']

        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
        cmd = 'INSERT INTO tb_conta_empresa(nme_empresa, senha_empresa, cnpj, regiao_atuacao, url) VALUES (%s, %s, %s, %s, %s);'

        mysql.executar(cmd, [nme_empresa, password, cnpj, reg_atuacao, url])
