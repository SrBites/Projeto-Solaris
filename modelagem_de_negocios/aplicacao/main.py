import os
from flask import Flask, render_template

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(template_dir)
template_dir = os.path.join(template_dir, 'modelagem_de_negocios')
template_dir = os.path.join(template_dir, 'interface')
template_dir = os.path.join(template_dir, 'templates')
print(template_dir)
# hard coded absolute path for testing purposes
working = 'c:\\Users\\tetia\\OneDrive\\Área de Trabalho\\solaris\\Projeto-Solaris\\modelagem_de_negocios\\interface\\templates'
print(working == template_dir)
app = Flask(__name__, template_folder=template_dir)

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