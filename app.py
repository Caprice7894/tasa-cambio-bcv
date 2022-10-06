import subprocess as sp
from flask import Flask
from flask import ( jsonify, render_template, url_for )
from datetime import datetime as dt
from scrapper import getDivisas

app = Flask(__name__)

def formatDivisas():
    divisas = ['EUR','CNY','TRY','RUB','USD']
    divisasNuevas = {}
    valores = getDivisas()
    indiceDivisa = 0
    for valor in valores:
        keyDivisa = divisas[indiceDivisa]
        divisasNuevas[keyDivisa] = float(valor)
        indiceDivisa += 1
    return {'divisas': divisasNuevas, 'fecha': dt.now()}

@app.get('/')
def divisas():
    divisas = formatDivisas()
    return jsonify(divisas)

@app.get('/home')
def home():
    result = formatDivisas()
    return render_template('base.html', divisa=result['divisas'], timestamp=result['fecha'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
