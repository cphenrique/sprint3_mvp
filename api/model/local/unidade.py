from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Unidade(Base):
    __tablename__ = 'unidade'

    id = Column("unidade_id", Integer, primary_key=True)
    nome = Column(String(128), unique=True)

    empresa_id = Column(Integer, ForeignKey('empresa.empresa_id'), nullable=False)

    areas = relationship('Area', backref='unidade')

    def __init__(self, nome:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.nome = nome