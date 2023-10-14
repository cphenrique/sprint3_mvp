from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Processo(Base):
    __tablename__ = 'processo'

    id = Column("processo_id", Integer, primary_key=True, autoincrement=True)
    processo = Column(String(128), unique=True)
    descricao = Column(String(1024))

    atividades = relationship('Atividade', backref='processo', lazy='dynamic')

    def __init__(self, processo:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.processo = processo
        self.descricao = descricao