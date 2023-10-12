from sqlalchemy import Column, ForeignKey, String, Integer

from  model import Base

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column("atividade_id", Integer, primary_key=True)
    atividade = Column(String(128), unique=True)
    descricao = Column(String(1024))

    super_atividade_id = Column(Integer, ForeignKey('atividade.atividade_id'))

    processo_id = Column(Integer, ForeignKey('processo.processo_id'), nullable=False)

    def __init__(self, processo_id:int, super_atividade_id:int, atividade:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.processo_id = processo_id
        self.super_atividade_id = super_atividade_id
        self.atividade = atividade
        self.descricao = descricao