from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session

from schemas import *

from route import *

from logger import logger

from flask_cors import CORS

info = Info(title="Tickets de CSC", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha o estilo de documentação.
    """
    return redirect('/openapi/swagger')

# configura as rotas para o Atendimento
configure_analista_routes(app)
configure_processo_routes(app)
configure_atividade_routes(app)

# configura as rotas para o Ticket
# configure_ticket_routes(app)
configure_estado_routes(app)
configure_prioridade_routes(app)
# configure_formulario_routes(app)
# configure_campo_routes(app)
# configure_valor_routes(app)