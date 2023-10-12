from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Campo(Base):
    __tablename__ = 'campo'

    id = Column("campo_id", Integer, primary_key=True)
    campo = Column(String(128), unique=True, nullable=False)
    tipo = Column(String(128), nullable=False)
    descricao = Column(String(1024))

    def __init__(self):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """