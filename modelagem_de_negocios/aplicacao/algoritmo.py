from flask import request
from modelagem_de_negocios.util import bd
import math

class IndicieSolarimetrico:
    def getIndicie(self, sgl):
        sgl_estado = sgl
        mysql = bd.SQL('Ce5tvx5KvM', 'xq09k27yty', 'Ce5tvx5KvM')

        cmd = 'SELECT * FROM tb_mapa_incidencia WHERE sgl_estado=%s'
        estado = mysql.sessao(cmd, [sgl_estado])

        return estado[3]

class Proposta:
    def calculo(self):
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

        cep = int(request.form['cep'])      # <------------------------ MUDAR ISSO AQUI

        recuo = 0
        solar = float(0.0)
        ind_solar = IndicieSolarimetrico()

        if sis == 'Monofásico':
            recuo = 30
        elif sis == 'Bifásico':
            recuo = 50
        elif sis == 'Trifásico':
            recuo = 100

        if 69900000 < cep < 69999999: #AC
            solar = ind_solar.getIndicie('AC')

        elif 57000000 < cep < 57999999: #AL
            solar = ind_solar.getIndicie('AL')

        elif 68900000 < cep < 68999999: #AP
            solar = ind_solar.getIndicie('AP')

        elif 69000000 < cep < 69299999 or 69400 - 000 < cep < 69899999: #AM
            solar = ind_solar.getIndicie('AM')

        elif 40000000 < cep < 48999999: #BA
            solar = ind_solar.getIndicie('BA')

        elif 60000000 < cep < 63999999: #CE
            solar = ind_solar.getIndicie('CE')

        elif 70000000 < cep < 72799999 or 73000000 < cep < 73699999: #DF
            solar = ind_solar.getIndicie('DF')

        elif 29000000 < cep < 29999999: #ES
            solar = ind_solar.getIndicie('ES')

        elif 72800000 < cep < 72999 - 999 or 73700000 < cep < 76799999: #GO
            solar = ind_solar.getIndicie('GO')

        elif 65000000 < cep < 65999999: #MA
            solar = ind_solar.getIndicie('MA')

        elif 79000000 < cep < 79999999: #MS
            solar = ind_solar.getIndicie('MS')

        elif 78000000 < cep < 78899999: #MT
            solar = ind_solar.getIndicie('MT')

        elif 30000000 < cep < 39999999: #MG
            solar = ind_solar.getIndicie('MG')

        elif 66000000 < cep < 68899999: #PA
            solar = ind_solar.getIndicie('PA')

        elif 58000000 < cep < 58999999: #PB
            solar = ind_solar.getIndicie('PB')

        elif 80000000 < cep < 87999999: #PR
            solar = ind_solar.getIndicie('PR')

        elif 50000000 < cep < 56999999: #PE
            solar = ind_solar.getIndicie('PE')

        elif 64000000 < cep < 64999999: #PI
            solar = ind_solar.getIndicie('PI')

        elif 20000000 < cep < 28999999: #RJ
            solar = ind_solar.getIndicie('RJ')

        elif 59000000 < cep < 59999999: #RN
            solar = ind_solar.getIndicie('RN')

        elif 90000000 < cep < 99999999: #RS
            solar = ind_solar.getIndicie('RS')

        elif 76800000 < cep < 76999999: #RO
            solar = ind_solar.getIndicie('RO')

        elif 69300000 < cep < 69399999: #RR
            solar = ind_solar.getIndicie('RR')

        elif 88000000 < cep < 89999999: #SC
            solar = ind_solar.getIndicie('SC')

        elif 1000000 < cep < 19999999: #SP
            solar = ind_solar.getIndicie('SP')

        elif 49000000 < cep < 49999999: #SE
            ssolar = ind_solar.getIndicie('SE')

        elif 77000000 < cep < 77999999: #TO
            solar = ind_solar.getIndicie('TO')

        media_mes = 30.41
        eficiencia = 1
        meta = (((m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12) / 12) - recuo)

        KWh = solar * media_mes * eficiencia
        KWp = meta / KWh

        #Placas de 400w
        qnt_400 = math.ceil(KWp / 0.4)

        #Placas de 500w
        qnt_500 = math.ceil(KWp / 0.5)

        rep = ''

        rep += f'<p>São necessarias:{qnt_400:.0f} placas de 400w para suprir seus recursos</p>\n'
        rep += f'<p>ou...</p>\n'
        rep += f'<p>{qnt_500:.0f} placas de 500w</p>\n'
        rep += f'<p>Isto é um valor aproximado, sempre consulte um especialista para confirmar e avaliar sua residencia!</p>\n'

        return rep