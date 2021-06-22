from flask import request
from modelagem_de_negocios.util import bd
import re

def tipoUsuario(usuario):
    usuario = usuario

    mysql = bd.SQL('root', '', 'ce5tvx5kvm')
    cmd = 'SELECT tipo_perfil FROM tb_conta_cliente WHERE nme_cliente=%s'
    cs = mysql.consultar(cmd, [usuario])
    tipocliente = cs.fetchone()

    cmd = 'SELECT tipo_perfil FROM tb_conta_empresa WHERE nme_empresa=%s'
    cs = mysql.consultar(cmd, [usuario])
    tipoempresa = cs.fetchone()

    if tipocliente != None:
        tipo_perfil = 1
    elif tipoempresa != None:
        tipo_perfil = 2
    else:
        tipo_perfil = 0

    return tipo_perfil

def validaSenha(senha):
    senha = senha
    while True:
        if (len(senha) < 8):
            flag = -1
            break
        elif not re.search("[a-zA-Z]", senha):
            flag = -1
            break
        elif not re.search("[0-9]", senha):
            flag = -1
            break
        elif not re.search("[_@$]", senha):
            flag = -1
            break
        else:
            flag = 0
            break

    return flag

def validaUsuario(usuario):
    usuario = usuario
    tipo_perfil = tipoUsuario(usuario)

    if tipo_perfil == 0:
        return True
    else:
        return False

class ContaCliente:
    def cadastra(self):
        nme_cliente = request.form['nme_cliente']
        senha = request.form['senha']
        cep = request.form['cep']

        user = 'usuario_invalido'
        password = 'senha_invalida'

        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = 'INSERT INTO tb_conta_cliente(nme_cliente, senha_cliente, cep_cliente) VALUES (%s, %s, %s);'

        if validaUsuario(nme_cliente):
            if validaSenha(senha) == 0:
                mysql.executar(cmd, [nme_cliente, senha, cep])
            else:
                return password
        else:
            return user

class ContaEmpresa:
    def cadastra(self):
        nme_empresa = request.form['nme_empresa']
        cnpj = request.form['cnpj']
        reg_atuacao = request.form['atuacao']
        senha = request.form['senha']
        url = request.form['link']

        user = 'usuario_invalido'
        password = 'senha_invalida'

        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = 'INSERT INTO tb_conta_empresa(nme_empresa, senha_empresa, cnpj, regiao_atuacao, url) VALUES (%s, %s, %s, %s, %s);'

        if validaUsuario(nme_empresa):
            if validaSenha(senha) == 0:
                mysql.executar(cmd, [nme_empresa, senha, cnpj, reg_atuacao, url])
            else:
                return password
        else:
            return user