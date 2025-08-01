from flask import Flask, redirect, render_template, request
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['dados_login'] = []
app.config['UPLOAD_FOLDER'] = 'static/uploads'
 
# Certifique-se de que a pasta de upload exista
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/variavel')
def variavel():
    return render_template('variavel.html')

@app.route('/comparacao')    
def comparacao():
    return render_template('comparacao.html')

@app.route('/educacao')
def educacao():
    return render_template('educacao.html')

@app.route('/meta_estudos.html')
def estudos():
    return render_template('meta_estudos.html')

@app.route('/casa.html')
def casa():
    return render_template('casa.html')

@app.route('/carro.html')
def carro():
    return render_template('carro.html')

@app.route('/viagem.html')
def viagem():
    return render_template('viagem.html')

@app.route('/voltar')
def voltar():
    return redirect('/home')

app.run(host= '127.0.0.1', port=80, debug=True)

