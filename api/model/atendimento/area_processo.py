from sqlalchemy import Table, Column, ForeignKey, Integer

from model import Base

area_processo = Table('area_processo',
                          Base.metadata,
                          Column('area_id', Integer, ForeignKey('area.area_id')),
                          Column('processo_id', Integer, ForeignKey('processo.processo_id')))