from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

from model.atendimento.analista_processo import analista_processo

class Analista(Base):
    __tablename__ = 'analista'

    id = Column("analista_id", Integer, primary_key=True)
    nome = Column(String(128))
    sobrenome = Column(String(128))
    usuario = Column(String(128), unique=True)
    email = Column(String(128), unique=True)

    area_id = Column(Integer, ForeignKey('area.area_id'), nullable=False)
    
    processos = relationship('Processo', secondary=analista_processo, backref='analistas')

    def __init__(self, nome:str, sobrenome:str, usuario:str, email:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario
        self.email = email