from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

from model.analista.analista_processo import analista_processo

class Analista(Base):
    __tablename__ = 'analista'

    id = Column("analista_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)
    usuario = Column(String(128), unique=True)
    email = Column(String(128), unique=True)

    processos = relationship('Processo', secondary=analista_processo, backref='analistas')

    def __init__(self, nome:str, usuario:str, email:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome
        self.usuario = usuario
        self.email = email