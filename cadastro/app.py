from flask import Flask, render_template, request
import requests

from models import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    tabela = request.args.get('tabela')
    if tabela:

        api_url = f'http://192.168.0.16:5000/{tabela}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
        return render_template('index.html', data=data, tabela=tabela)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)