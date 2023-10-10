from pydantic import BaseModel
from typing import List
from model import Campo


class CampoSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1


class CampoViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1


class ListagemCamposSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    campos:List[CampoSchema]


class CampoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class CampoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_campos(campos: List[Campo]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for campo in campos:
        result.append(
            {
                "id": campo.id
            }
        )
    return {"campos": result}


def apresenta_campo(campo: Campo):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": campo.id
    }