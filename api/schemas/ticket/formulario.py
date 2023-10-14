from pydantic import BaseModel
from typing import List
from model import Formulario


class FormularioSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    campo_id: int = 1


class FormularioViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    campo_id: int = 1


class ListagemFormulariosSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    formularios:List[FormularioSchema]


class FormularioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class FormularioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_formularios(formularios: List[Formulario]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for formulario in formularios:
        result.append(
            {
                "id": formulario.id,
                "formulario_campos": [f.indice for f in formulario.formulario_campos],
                "campos": [[f.id, f.campo, f.tipo] for f in formulario.campos]
            }
        )
    return {"formularios": result}


def apresenta_formulario(formulario: Formulario):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": formulario.id,
        "formulario_campos": [f.indice for f in formulario.formulario_campos],
        "campos": [[f.id, f.campo, f.tipo] for f in formulario.campos]
    }