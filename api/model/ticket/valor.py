from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from  model import Base

class Valor(Base):
    __tablename__ = 'valor'

    id = Column("valor_id", Integer, primary_key=True)
    
    campo_id = Column(Integer, ForeignKey('campo.campo_id'), nullable=False)
    ticket_id = Column(Integer, ForeignKey('ticket.ticket_id'), nullable=False)

    def __init__(self):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """