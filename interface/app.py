from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/cadastro')
def cadastro():
   return render_template('cadastro.html')

@app.route('/')
def index():
   return render_template('index.html')


app.run()