from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column("ticket_id", Integer, primary_key=True)
    
    analista_id = Column(Integer, ForeignKey('analista.analista_id'), nullable=False)
    formulario_id = Column(Integer, ForeignKey('formulario.formulario_id'), nullable=False)
    prioridade_id = Column(Integer, ForeignKey('prioridade.prioridade_id'), nullable=False)
    estado_id = Column(Integer, ForeignKey('prioridade.prioridade_id'), nullable=False)


    def __init__(self):
        """

        Cria um analista de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """