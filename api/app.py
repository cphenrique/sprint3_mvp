from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session
from model import Analista, Processo, Atividade

from schemas import *

from route import *

from logger import logger

from flask_cors import CORS

info = Info(title="Tickets de CSC", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha o estilo de documentação.
    """
    return redirect('/openapi/swagger')


configure_analista_routes(app)
configure_processo_routes(app)
configure_atividade_routes(app)