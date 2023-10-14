from pydantic import BaseModel
from typing import List
from model import Estado


class EstadoSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    estado: str = "Aberto"


class EstadoViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    estado: str = "Aberto"


class ListagemEstadosSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    estados:List[EstadoSchema]


class EstadoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class EstadoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_estados(estados: List[Estado]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for estado in estados:
        result.append(
            {
                "id": estado.id,
                "estado": estado.estado
            }
        )
    return {"estados": result}


def apresenta_estado(estado: Estado):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": estado.id,
        "estado": estado.estado
    }