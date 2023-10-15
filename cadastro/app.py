from flask import Flask, render_template, redirect, url_for, request, jsonify, json
from flask_wtf.csrf import CSRFProtect
import requests

from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TBD'
csrf = CSRFProtect(app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/analistas')   
def get_analistas():
    form = AnalistaForm()
    api_url = "http://localhost:5000/get_analistas"
    response = requests.get(api_url)
    if response.status_code == 200:
        analistas_json = response.json()
    return render_template('analistas.html', analistas=analistas_json['analistas'], form=form)

@app.route('/add_analista', methods=['POST'])
def add_analista():
    api_url = 'http://macbook-air.local:5000/add_analista'
    response = requests.post(url=api_url, data=request.form)
    print(response.status_code, response.reason, response.text)
    return redirect(url_for('get_analistas'))

@app.route('/del_analista/<int:id>', methods=['GET'])
def del_analista(id):
    api_url = f'http://macbook-air.local:5000/del_analista?id={id}' 
    response = requests.delete(url=api_url)
    print(response.status_code, response.reason, response.text)
    return redirect(url_for('get_analistas'))

if __name__ == '__main__':
    app.run(debug=True)