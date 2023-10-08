from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Analista


class AnalistaSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Pedro Costa"
    usuario: str = "pcosta"
    email: str = "pedro.costa@tck.com"


class AnalistaViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Pedro Costa"
    usuario: str = "pcosta"
    email: str = "pedro.costa@tck.com"


class AnalistaBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Pedro Costa"


class AnalistaBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = 1


class ListagemAnalistasSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    analistas:List[AnalistaSchema]


class AnalistaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class AnalistaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_analistas(analistas: List[Analista]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for analista in analistas:
        result.append(
            {
                "id": analista.id,
                "nome": analista.nome,
                "usuario": analista.usuario,
                "email": analista.email
            }
        )
    return {"analistas": result}


def apresenta_analista(analista: Analista):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": analista.id,
        "nome": analista.nome,
        "usuario": analista.usuario,
        "email": analista.email
    }