from pydantic import BaseModel
from typing import List
from model import Valor


class ValorSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    valor: str = "Valor"
    campo_id: int = 1
    ticket_id: int = 1


class ValorViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    valor: str = "Valor"
    campo_id: int = 1
    ticket_id: int = 1


class ListagemValoresSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    valores:List[ValorSchema]


class ValorBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class ValorDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_valores(valores: List[Valor]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for valor in valores:
        result.append(
            {
                "id": valor.id,
                "valor": valor.valor,
                "campo_id": valor.campo_id,
                "ticket_id": valor.ticket_id
            }
        )
    return {"valores": result}


def apresenta_valor(valor: Valor):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": valor.id,
        "valor": valor.valor,
        "campo_id": valor.campo_id,
        "ticket_id": valor.ticket_id
    }