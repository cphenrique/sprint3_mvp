from sqlalchemy import Column, ForeignKey, String, Integer

from  model import Base

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column("atividade_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)
    descricao = Column(String(1024))

    processo_id = Column(Integer, ForeignKey('processo.processo_id'), nullable=False)

    def __init__(self, nome:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome
        self.descricao = descricao