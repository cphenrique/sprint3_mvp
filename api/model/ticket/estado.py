from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship

from model import Base

class Estado(Base):
    __tablename__ = 'estado'

    id = Column("estado_id", Integer, primary_key=True)
    estado = Column(String, unique=True, nullable=False)

    def __init__(self, estado:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.estado = estado