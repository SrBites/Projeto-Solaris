import os
from flask import render_template
from modelagem_de_negocios.util import pathing

rota = pathing.Path()
app = rota.daWay()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

app.run()