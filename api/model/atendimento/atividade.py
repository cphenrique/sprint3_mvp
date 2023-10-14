from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from  model import Base

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column("atividade_id", Integer, primary_key=True, autoincrement=True)
    atividade = Column(String(128), unique=True)
    descricao = Column(String(1024))

    processo_id = Column(Integer, ForeignKey('processo.processo_id'), nullable=False)

    #formularios = relationship('Formulario', backref='atividade', lazy='dynamic')

    def __init__(self, processo_id:int, atividade:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.processo_id = processo_id
        self.atividade = atividade
        self.descricao = descricao