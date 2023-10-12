from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

from model.atendimento.analista_processo import analista_processo

class Analista(Base):
    __tablename__ = 'analista'

    id = Column("analista_id", Integer, primary_key=True)
    nome = Column(String(128), nullable=False)
    sobrenome = Column(String(128), nullable=False)
    usuario = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)

    area_id = Column(Integer, ForeignKey('area.area_id'), nullable=False)
    
    processos = relationship('Processo', secondary=analista_processo, backref='analistas')

    def __init__(self, area_id:int, nome:str, sobrenome:str, usuario:str, email:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.area_id = area_id
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario
        self.email = email