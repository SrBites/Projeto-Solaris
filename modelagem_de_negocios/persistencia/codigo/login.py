from flask import request
from modelagem_de_negocios.util import bd

class LoginCliente:
    def loga(self):
        username = request.form['username']
        password = request.form['senha']
        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

        cmd = '''SELECT * FROM tb_conta_cliente
        WHERE nme_cliente=%s AND senha_cliente=%s;
        '''
        verificaLogin = mysql.login(cmd, [username, password])

        try:
            if username in verificaLogin and password in verificaLogin:
                print('Login de cliente efetuado com sucesso!')
                return True
        except:
            print('Usuário ou senha errados!')
            return False

class LoginEmpresa:
    def loga(self):
        username = request.form['username']
        password = request.form['senha']
        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

        cmd = '''SELECT * FROM tb_conta_empresa
        WHERE nme_empresa=%s AND senha_emprea=%s;
        '''
        verificaLogin = mysql.login(cmd, [username, password])

        try:
            if username in verificaLogin and password in verificaLogin:
                print('Login de empresa efetuado com sucesso!')
                return True
        except:
            print('Usuário ou senha errados!')
            return False