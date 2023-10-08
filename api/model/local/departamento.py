from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from  model import Base

class Departamento(Base):
    __tablename__ = 'departamento'

    id = Column("departamento_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)

    area_id = Column(Integer, ForeignKey('area.area_id'), nullable=False)

    #departamentos = relationship('Departamento', backref='area')

    def __init__(self, nome:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome