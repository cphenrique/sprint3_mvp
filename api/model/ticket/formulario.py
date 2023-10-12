from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Formulario(Base):
    __tablename__ = 'formulario'

    id = Column("formulario_id", Integer, primary_key=True)

    atividade_id = Column(Integer, ForeignKey('atividade.atividade_id'), nullable=False)
    
    def __init__(self):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """