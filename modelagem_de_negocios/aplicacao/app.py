from flask import Flask, render_template, request
app = Flask(__name__)
import math
# versão 1.1

@app.route('/')
def index():
    # um template generico apenas para testar o funcionamento do calculo
    # templates/numeros.html
    return render_template('algoritmo.html')


# OPERACOES.HTML
@app.route('/proposta', methods=['POST'])
def nome():
    # Recuperando dados do formulário de index() e dados necessarios (n1 a n12 necessita estar em Kwh)
    '''
    indicie solarimetrico:
    acre-4,56
    alagoas-5,35
    amapa-4,73
    amazonas-4,36
    bahia-5,19
    ceara-5,67
    espirito santo-5,53
    goias-5,27
    maranhao-5,10
    mato grosso-4,99
    mato grosso do sul-4,97
    minas gerais-5,59
    para-4,59
    paraiba-5,62
    parana-4,79
    pernambuco-5,75
    piaui-5,78
    rio de janeiro-4,73
    rio grande do norte-5,98
    rio grande do sul-4,57
    rondonia-4,56
    roraima-4,90
    santa catarina-4,36
    sao paulo-4,45
    sergipe-5,27
    tocantins-5,22
    DF-5,39

    dias em um mês(media):
    30,41

    coeficiente de eficiencia(distancia,sombra,cabeamento,eventos):
    90%(0.9)

    tipo de fase:
    monofasico, bifasico, trifasico

    media de consumo mensal do cliente(KWh):
    12 contas de luz / 12 = x

    consumo minimo imposto(y):
    mono--> 30KWh
    bi  --> 50KWh
    tri --> 100KWh

    geração ideal:
    G = x - y

    Radiação local * 30,41(media dias no mes) * 0,9(eficiencia) = Z = KWh gerado com 1 KWP de potencia

    G / z = KWP de potencia do sistema(arredondar para cima)

    (quantidade de placas * voltagem)/100 = KWP de potencia

    '''
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

    # como não existe conta cliente, não é possivel acessar os dados como o cep, por isso utilizei o request
    # porém,originalmente ele virá do banco de dados da conta cliente
    
    cep = int(request.form['cep'])
    
    solar = float(0.0)
    recuo = 0

    if sis == 'Monofásico':
        recuo = 30
    elif sis == 'Bifásico':
        recuo = 50
    elif sis == 'Trifásico':
        recuo = 100

    # identificando o indice pelo cep(sem o '-' para facilitar no teste do calculo)
    if 70000000 < cep < 72799999 or 73000000 < cep < 73699999:
        solar = 5.39
        #df 1/ 2

    if 69900000 < cep < 69999999:
        solar = 4.56
        #acre

    if 57000000 < cep < 57999999:
        solar = 5.35
        # alagoas

    if 69000000 < cep < 69299999 or 69400-000 < cep < 69899999:
        solar = 4.36
        #amazonas 1/2

    if 68900000 < cep < 68999999:
        solar = 4.73
        #amapa

    if 40000000 < cep < 48999999:
        solar = 5.19
        #bahia

    if 60000000 < cep < 63999999:
        solar = 5.67
        #Ceará

    if 29000000 < cep < 29999999:
        solar = 5.53
        #espirito santo

    if 72800000 < cep < 72999-999 or 73700000 < cep < 76799999:
        solar = 5.27
        #goias 1/2

    if 65000000 < cep < 65999999:
        solar = 5.10
        #maranhao

    if 30000000 < cep < 39999999:
        solar = 5.59
        #minas gerais

    if 79000000 < cep < 79999999:
        solar = 4.97
        #mato grosso do sul

    if 78000000 < cep < 78899999:
        solar = 4.99
        #mato grosso

    if 66000000 < cep < 68899999:
        solar = 4.59
        #pará

    if 58000000 < cep < 58999999:
        solar = 5.62
        #paraíba

    if 50000000 < cep < 56999999:
        solar = 5.75
        #pernambuco

    if 64000000 < cep < 64999999:
        solar = 5.78
        #piauí

    if 80000000 < cep < 87999999:
        solar = 4.79
        #paraná

    if 20000000 < cep < 28999999:
        solar = 4.73
        #rio de janeiro

    if 59000000 < cep < 59999999:
        solar = 5.98
        #rio grande do norte

    if 76800000 < cep < 76999999:
        solar = 4.56
        #rondonia

    if 69300000 < cep < 69399999:
        solar = 4.90
        #roraima

    if 90000000 < cep < 99999999:
        solar = 4.57
        #rio grande do sul

    if 80000000 < cep < 87999999:
        solar = 4.79
        #paraná

    if 88000000 < cep < 89999999:
        solar = 4.36
        #santa catarina

    if 49000000 < cep < 49999999:
        solar = 5.27
        #segipe

    if 1000000 < cep < 19999999:
        solar = 4.45
        #são paulo

    if 77000000 < cep < 77999999:
        solar = 5.22
        #tocantins




    # processamento
    media_mes = 30.41
    eficiencia = 1
    meta = (((m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12)/12) - recuo)

    KWh = solar * media_mes * eficiencia
    KWp = meta/KWh

    # placas de 480w
    qnt_400 = math.ceil(KWp / 0.48)

    # placas de 500w
    qnt_500 = math.ceil(KWp / 0.5)

    rep = ''

    rep += f'<p>São necessarias:{qnt_400:.0f} placas de 400w para suprir seus recursos</p>\n'
    rep += f'<p>ou...</p>\n'
    rep += f'<p>{qnt_500:.0f} placas de 500w</p>\n'
    rep += f'<p>Isto é um valor aproximado, sempre consulte um especialista para confirmar e avaliar sua residencia!</p>\n'

    # templates/operacoes.html
    return render_template('proposta.html', rep=rep)

app.run()