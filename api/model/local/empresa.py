from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column("empresa_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True, nullable=False)
    descricao = Column(String(1024))
    logo = Column(String(128), nullable=False)

    unidades = relationship('Unidade', backref='empresa')

    def __init__(self, nome:str, descricao:str, logo:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome
        self.descricao = descricao
        self.logo = logo