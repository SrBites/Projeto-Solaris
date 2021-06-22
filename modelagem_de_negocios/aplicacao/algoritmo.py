from flask import request
from modelagem_de_negocios.util import bd
import math

class IndicieSolarimetrico:
    def getIndicie(self, sgl):
        sgl_estado = sgl
        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = 'SELECT * FROM tb_mapa_incidencia WHERE sgl_estado=%s'
        cs = mysql.consultar(cmd, [sgl_estado])
        estado = cs.fetchone()

        return estado[3]

class Proposta:
    def validacaoCEP(self, cep):
        ind_solar = IndicieSolarimetrico()
        if 69900000 < cep < 69999999:  # AC
            solar = ind_solar.getIndicie('AC')
            estado = "AC"

        elif 57000000 < cep < 57999999:  # AL
            solar = ind_solar.getIndicie('AL')
            estado = "AL"

        elif 68900000 < cep < 68999999:  # AP
            solar = ind_solar.getIndicie('AP')
            estado = "AP"

        elif 69000000 < cep < 69299999 or 69400 - 000 < cep < 69899999:  # AM
            solar = ind_solar.getIndicie('AM')
            estado = "AM"

        elif 40000000 < cep < 48999999:  # BA
            solar = ind_solar.getIndicie('BA')
            estado = "BA"

        elif 60000000 < cep < 63999999:  # CE
            solar = ind_solar.getIndicie('CE')
            estado = "CE"

        elif 70000000 < cep < 72799999 or 73000000 < cep < 73699999:  # DF
            solar = ind_solar.getIndicie('DF')
            estado = "DF"

        elif 29000000 < cep < 29999999:  # ES
            solar = ind_solar.getIndicie('ES')
            estado = "ES"

        elif 72800000 < cep < 72999 - 999 or 73700000 < cep < 76799999:  # GO
            solar = ind_solar.getIndicie('GO')
            estado = "GO"

        elif 65000000 < cep < 65999999:  # MA
            solar = ind_solar.getIndicie('MA')
            estado = "MA"

        elif 79000000 < cep < 79999999:  # MS
            solar = ind_solar.getIndicie('MS')
            estado = "MS"

        elif 78000000 < cep < 78899999:  # MT
            solar = ind_solar.getIndicie('MT')
            estado = "MT"

        elif 30000000 < cep < 39999999:  # MG
            solar = ind_solar.getIndicie('MG')
            estado = "MG"

        elif 66000000 < cep < 68899999:  # PA
            solar = ind_solar.getIndicie('PA')
            estado = "PA"

        elif 58000000 < cep < 58999999:  # PB
            solar = ind_solar.getIndicie('PB')
            estado = "PB"

        elif 80000000 < cep < 87999999:  # PR
            solar = ind_solar.getIndicie('PR')
            estado = "PR"

        elif 50000000 < cep < 56999999:  # PE
            solar = ind_solar.getIndicie('PE')
            estado = "PE"

        elif 64000000 < cep < 64999999:  # PI
            solar = ind_solar.getIndicie('PI')
            estado = "PI"

        elif 20000000 < cep < 28999999:  # RJ
            solar = ind_solar.getIndicie('RJ')
            estado = "RJ"

        elif 59000000 < cep < 59999999:  # RN
            solar = ind_solar.getIndicie('RN')
            estado = "RN"

        elif 90000000 < cep < 99999999:  # RS
            solar = ind_solar.getIndicie('RS')
            estado = "RS"

        elif 76800000 < cep < 76999999:  # RO
            solar = ind_solar.getIndicie('RO')
            estado = "RO"

        elif 69300000 < cep < 69399999:  # RR
            solar = ind_solar.getIndicie('RR')
            estado = "RR"

        elif 88000000 < cep < 89999999:  # SC
            solar = ind_solar.getIndicie('SC')
            estado = "SC"

        elif 1000000 < cep < 19999999:  # SP
            solar = ind_solar.getIndicie('SP')
            estado = "SP"

        elif 49000000 < cep < 49999999:  # SE
            solar = ind_solar.getIndicie('SE')
            estado = "SE"

        elif 77000000 < cep < 77999999:  # TO
            solar = ind_solar.getIndicie('TO')
            estado = "TO"

        else:
            solar = 0.0
            estado = "N/A"

        return [solar, estado]

    def updateDados(self, idt):
        nme = request.form['nome']
        url = request.form['url']
        regiao = request.form['regiao']
        descricao = request.form['descricao']
        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = '''UPDATE tb_conta_empresa SET nme_empresa=%s, regiao_atuacao=%s, url=%s, descricao=%s 
                 WHERE id_conta_empresa=%s'''

        cs = mysql.executar(cmd, [nme, regiao, url, descricao, idt])
        msg = ''
        if cs:
            msg += f'Alteração da empresa {nme} concluída com sucesso'
            return msg
        msg += f'Alteração falhou'
        return msg



    def get_uma_empresa(self, idt):
        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = 'SELECT nme_empresa, regiao_atuacao, url, descricao FROM tb_conta_empresa WHERE id_conta_empresa=%s'
        cs = mysql.consultar(cmd, [idt])
        informacoes = cs.fetchone()
        return informacoes


    def getEmpresas(self, sgl):
        sgl_estado = sgl
        mysql = bd.SQL('root', '', 'ce5tvx5kvm')
        cmd = 'SELECT nme_empresa, regiao_atuacao, url, descricao FROM tb_conta_empresa WHERE regiao_atuacao=%s'
        cs = mysql.consultar(cmd, [sgl_estado])
        html = ''
        for [nme, regiao_atuacao, url, descricao] in cs:
            html += '<div class="col-md-4 mt-3 mb-3">'
            html += '<div class="card p-3">'
            html += '<div class="d-flex flex-row mb-3">'
            html += '<div class="d-flex flex-column ml-2">'
            html += f'<span>{nme}</span>'
            html += '</div>'
            html += '</div>'
            html += f'<h6>{descricao}</h6>'
            html += '<div class="d-flex justify-content-between install mt-3">'
            html += f'<span>Região: {regiao_atuacao}</span>'
            html += '<span class="text-primary">'
            html += f'<a href="{url}" class="text-warning">Link para a empresa&nbsp;</a>'
            html += '<i class="fa fa-angle-right"></i>'
            html += '</span>'
            html += '</div></div></div>'
        cs.close()
        return html

    def calculo(self, cep):
        m1 = int(request.form['m1'])
        m2 = int(request.form['m2'])
        m3 = int(request.form['m3'])
        m4 = int(request.form['m4'])
        m5 = int(request.form['m5'])
        m6 = int(request.form['m6'])
        m7 = int(request.form['m7'])
        m8 = int(request.form['m8'])
        m9 = int(request.form['m9'])
        m10 = int(request.form['m10'])
        m11 = int(request.form['m11'])
        m12 = int(request.form['m12'])
        sis = request.form['tiposis']

        cep = cep

        recuo = 0


        if sis == 'Monofásico':
            recuo = 30
        elif sis == 'Bifásico':
            recuo = 50
        elif sis == 'Trifásico':
            recuo = 100



        media_mes = 30.41
        eficiencia = 1
        meta = (((m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12) / 12) - recuo)
        proposta = Proposta()
        validacao = proposta.validacaoCEP(cep)
        solar = validacao[0]

        KWh = solar * media_mes * eficiencia
        KWp = meta / KWh

        #Placas de 400w
        qnt_400 = math.ceil(KWp / 0.4)

        #Placas de 500w
        qnt_500 = math.ceil(KWp / 0.5)

        rep = ''

        rep += f'<h1 class="display-6">São necessarias: {qnt_400:.0f} placas de 400w para suprir seus recursos</h1>\n'
        rep += f'<h1 class="display-6">ou...</h1>\n'
        rep += f'<h1 class="display-6">{qnt_500:.0f} placas de 500w</h1>\n'
        rep += f'<h1 class="display-6">Isto é um valor aproximado, sempre consulte um especialista para confirmar e avaliar sua residência!</h1>'

        return rep