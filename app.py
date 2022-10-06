import subprocess as sp
from flask import Flask
from flask import ( jsonify, render_template, url_for )
from datetime import datetime as dt

app = Flask(__name__)

def getDivisas():
    divisas = ['EUR','CNY','TRY','RUB','USD']
    divisasNuevas = {}
    with sp.Popen(['bash', './command.sh'], stdout=sp.PIPE) as proc:
        datos = proc.stdout.read()
        cadenaDatos = datos.decode('UTF-8').replace(',', '.')
        valores = cadenaDatos.split('\n')
        valores.pop()
        indiceDivisa = 0
        for valor in valores:
            keyDivisa = divisas[indiceDivisa]
            divisasNuevas[keyDivisa] = float(valor)
            indiceDivisa += 1
    return {'divisas': divisasNuevas, 'fecha': dt.now()}

@app.get('/')
def divisas():
    divisas = getDivisas()
    return jsonify(divisas)

@app.get('/home')
def home():
    result = getDivisas()
    return render_template('base.html', divisa=result['divisas'], timestamp=result['fecha'])

app.run(host='0.0.0.0', port=3000)
