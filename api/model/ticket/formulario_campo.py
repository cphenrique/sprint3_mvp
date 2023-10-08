from sqlalchemy import Table, Column, ForeignKey, Integer

from model import Base

formulario_campo = Table('formulario_campo',
                          Base.metadata,
                          Column('formulario_id', Integer, ForeignKey('formulario.formulario_id')),
                          Column('campo_id', Integer, ForeignKey('campo.campo_id')))