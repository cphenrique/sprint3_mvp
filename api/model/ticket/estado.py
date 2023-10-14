from sqlalchemy import Column, String, Integer

from model import Base

class Estado(Base):
    __tablename__ = 'estado'

    id = Column("estado_id", Integer, primary_key=True, autoincrement=True)
    estado = Column(String(128), unique=True, nullable=False)

    def __init__(self, estado:str):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.estado = estado