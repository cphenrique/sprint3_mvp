from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Unidade(Base):
    __tablename__ = 'unidade'

    id = Column("unidade_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)
    descricao = Column(String(1024), unique=True)
    logo = Column(String(128), unique=True)
    cor = Column(String(128), unique=True)
    acento = Column(String(128), unique=True)

    empresa_id = Column(Integer, ForeignKey('empresa.empresa_id'), nullable=False)

    areas = relationship('Area', backref='unidade')

    def __init__(self, empresa_id:int, nome:str, descricao:str, logo:str, cor:str, acento:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.empresa_id = empresa_id
        self.nome = nome
        self.descricao = descricao
        self.logo = logo
        self.cor = cor
        self.acento = acento