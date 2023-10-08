from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from  model import Base

class Area(Base):
    __tablename__ = 'area'

    id = Column("area_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)

    unidade_id = Column(Integer, ForeignKey('unidade.unidade_id'), nullable=False)

    departamentos = relationship('Departamento', backref='area')

    def __init__(self, nome:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome