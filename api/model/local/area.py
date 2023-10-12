from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from  model import Base

class Area(Base):
    __tablename__ = 'area'

    id = Column("area_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)
    descricao = Column(String(1024))

    unidade_id = Column(Integer, ForeignKey('unidade.unidade_id'), nullable=False)

    departamentos = relationship('Departamento', backref='area')

    def __init__(self, unidade_id:int, nome:str, descricao:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.unidade_id = unidade_id
        self.nome = nome
        self.descricao = descricao