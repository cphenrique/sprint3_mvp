from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    processos = []
    formulario = []
    formulario_id = request.args.get('formulario_id')
    
    api_url_processos = "http://localhost:5000/processos"
    response_processos = requests.get(api_url_processos)
    if response_processos.status_code == 200:
        processos = response_processos.json()

    if request.method == 'POST':

        api_url_formulario = f"http://localhost:5000/formulario?id={formulario_id}"
        response_formulario = requests.get(api_url_formulario)
        if response_formulario.status_code == 200:
            formulario = response_formulario.json()
    
    return render_template('index.html', processos=processos, formulario=formulario)


@app.route('/formulario/<formulario_id>', methods=['GET'])
def get_formulario(formulario_id):
    api_url_formulario = f"http://localhost:5000/formulario?id={formulario_id}"
    response_formulario = requests.get(api_url_formulario)
    if response_formulario.status_code == 200:
        formulario = response_formulario.json()
    
    return render_template('formulario.html', formulario=formulario)
    
if __name__ == '__main__':
    app.run(debug=True)