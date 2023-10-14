from pydantic import BaseModel
from typing import List
from model import Prioridade


class PrioridadeSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    prioridade: str = "Alta"


class PrioridadeViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    prioridade: str = "Alta"


class ListagemPrioridadesSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    prioridades:List[PrioridadeSchema]


class PrioridadeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class PrioridadeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_prioridades(prioridades: List[Prioridade]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for prioridade in prioridades:
        result.append(
            {
                "id": prioridade.id,
                "prioridade": prioridade.prioridade
            }
        )
    return {"prioridades": result}


def apresenta_prioridade(prioridade: Prioridade):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": prioridade.id,
        "prioridade": prioridade.prioridade
    }