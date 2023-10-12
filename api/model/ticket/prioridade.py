from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Prioridade(Base):
    __tablename__ = 'prioridade'

    id = Column("prioridade_id", Integer, primary_key=True)
    prioridade = Column(String(128), unique=True, nullable=False)

    def __init__(self, prioridade:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.prioridade = prioridade