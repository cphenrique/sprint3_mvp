from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc
import os

# importando os elementos definidos no modelo
from model.base import Base

from model.analista.analista import Analista
from model.analista.processo import Processo
from model.analista.atividade import Atividade
from model.analista.analista_processo import analista_processo

from model.local.empresa import Empresa
from model.local.unidade import Unidade
from model.local.area import Area
from model.local.departamento import Departamento

from model.ticket.ticket import Ticket
from model.ticket.formulario import Formulario
from model.ticket.campo import Campo
from model.ticket.formulario_campo import formulario_campo
from model.ticket.valor import Valor

# url de acesso ao banco
db_url = 'postgresql://postgres:1234@localhost:5432/ticket'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)