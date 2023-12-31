from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Analista(Base):
    __tablename__ = 'analista'

    id = Column("analista_id", Integer, primary_key=True, autoincrement=True)
    nome = Column(String(128), nullable=False)
    sobrenome = Column(String(128), nullable=False)
    usuario = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    

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