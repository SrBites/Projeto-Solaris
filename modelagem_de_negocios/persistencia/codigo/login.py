from flask import request
from modelagem_de_negocios.util import bd

class ContaCliente:
    def loga(self):

        username = str(request.form['username'])
        password = (request.form['senha'])

        cmd ='SELECT * FROM tb_conta_cliente WHERE nme_cliente=%s AND senha_cliente=%s;'

        print(username)
        print(password)

        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')



        '''
        try:
            mysql.consultar(cmd, [username, password])
        except:
            raise ValueError('deu merda')
            
         '''

'''
class ContaEmpresa:
    def loga(self):
'''