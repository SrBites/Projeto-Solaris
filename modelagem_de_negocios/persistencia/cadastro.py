from flask import request
from modelagem_de_negocios.util import bd
import re

def validaSenha(senha):
    password = senha
    while True:
        if (len(password) < 8):
            flag = -1
            break
        elif not re.search("[a-zA-Z]", password):
            flag = -1
            break

        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        else:
            flag = 0
            break

    return flag

def validaUsuarioCliente(usuario):
    user = usuario

    mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
    cmd = '''SELECT * FROM tb_conta_cliente WHERE nme_cliente=%s;'''
    cs = mysql.consultar(cmd, [user])
    valida = cs.fetchone()

    if valida == None:
        return True
    else:
        return False

class ContaCliente:
    def cadastra(self):
        username = request.form['nme_cliente']
        password = request.form['senha']
        cep = request.form['cep']

        if validaUsuarioCliente(username):
            if validaSenha(password) == 0:
                mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
                cmd = 'INSERT INTO tb_conta_cliente(nme_cliente, senha_cliente, cep_cliente) VALUES (%s, %s, %s);'

                mysql.executar(cmd, [username, password, cep])

        else:
            return False

class ContaEmpresa:
    def cadastra(self):
        nme_empresa = request.form['nme_empresa']
        cnpj = request.form['cnpj']
        reg_atuacao = request.form['atuacao']
        password = request.form['senha']
        url = request.form['link']

        if validaSenha(password) == 0:
            mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')
            cmd = 'INSERT INTO tb_conta_empresa(nme_empresa, senha_empresa, cnpj, regiao_atuacao, url) VALUES (%s, %s, %s, %s, %s);'

            mysql.executar(cmd, [nme_empresa, password, cnpj, reg_atuacao, url])
        else:
            return False