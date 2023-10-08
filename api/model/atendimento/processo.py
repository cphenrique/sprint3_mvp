from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

from model.atendimento.analista_processo import analista_processo

class Processo(Base):
    __tablename__ = 'processo'

    id = Column("processo_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)
    descricao = Column(String(1024))

    #analistas = relationship('Analista', secondary=analista_processo, backref='processos')

    atividades = relationship('Atividade', backref='processo')

    def __init__(self, nome:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome
        self.descricao = descricao