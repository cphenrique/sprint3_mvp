from sqlalchemy import Column, String, Integer

from model import Base

class Prioridade(Base):
    __tablename__ = 'prioridade'

    id = Column("prioridade_id", Integer, primary_key=True, autoincrement=True)
    prioridade = Column(String(128), unique=True, nullable=False)

    def __init__(self, prioridade:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.prioridade = prioridade