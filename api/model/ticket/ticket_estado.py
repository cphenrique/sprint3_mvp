from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime
from datetime import datetime

from model import Base

ticket_estado = Table('ticket_estado',
                          Base.metadata,
                          Column('ticket_id', Integer, ForeignKey('ticket.ticket_id')),
                          Column('estado_id', Integer, ForeignKey('estado.estado_id')),
                          Column('dt_insercao', DateTime, default=datetime.now()))