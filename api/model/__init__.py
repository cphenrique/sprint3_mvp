from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc
import os

# importando os elementos definidos no modelo
from model.base import Base

from model.atendimento.analista import Analista
from model.atendimento.atividade import Atividade
from model.atendimento.processo import Processo

from model.ticket.ticket import Ticket
from model.ticket.estado import Estado
from model.ticket.ticket_estado import ticket_estado
from model.ticket.prioridade import Prioridade
from model.ticket.formulario import Formulario
from model.ticket.campo import Campo
from model.ticket.formulario_campo import FormularioCampo
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