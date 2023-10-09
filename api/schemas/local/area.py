from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Area


class AreaSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Area"
    descricao: str = "Breve descrição da area."


class AreaViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Area"
    descricao: str = "Breve descrição da area."


class ListagemAreasSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    areas:List[AreaSchema]


class AreaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class AreaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_areas(areas: List[Area]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for area in areas:
        result.append(
            {
                "id": area.id,
                "nome": area.nome,
                "descricao": area.descricao
            }
        )
    return {"areas": result}


def apresenta_area(area: Area):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": area.id,
        "nome": area.nome,
        "descricao": area.descricao
    }