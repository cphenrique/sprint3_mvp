from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from model import Base, Formulario, Campo

class FormularioCampo(Base):
     __tablename__ = 'formulario_campo'
     id = Column("formulario_campo_id", Integer, primary_key=True)
     formulario_id = Column("formulario_id", Integer, ForeignKey('formulario.formulario_id'))
     campo_id = Column("campo_id", Integer, ForeignKey('campo.campo_id'))
     indice = Column("indice", Integer)

     formularios = relationship(Formulario, backref='formulario_campo')
     campos = relationship(Campo, backref='formulario_campo')