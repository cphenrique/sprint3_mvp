from sqlalchemy import Table, Column, ForeignKey, Integer

from model import Base

analista_processo = Table('analista_processo',
                          Base.metadata,
                          Column('analista_id', Integer, ForeignKey('analista.analista_id')),
                          Column('processo_id', Integer, ForeignKey('processo.processo_id')))