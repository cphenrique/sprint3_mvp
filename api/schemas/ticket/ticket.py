from pydantic import BaseModel
from typing import List
from model import Ticket


class TicketSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    analista_id: int = 1
    formulario_id: int = 1
    prioridade_id: int = 1


class TicketViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    analista_id: int = 1
    formulario_id: int = 1
    prioridade_id: int = 1


class ListagemTicketsSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    tickets:List[TicketSchema]


class TicketBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class TicketDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_tickets(tickets: List[Ticket]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for ticket in tickets:
        result.append(
            {
                "id": ticket.id,
                "analista_id": ticket.analista_id,
                "formulario_id": ticket.formulario_id,
                "prioridade_id": ticket.prioridade_id
            }
        )
    return {"tickets": result}


def apresenta_ticket(ticket: Ticket):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": ticket.id,
        "analista_id": ticket.analista_id,
        "formulario_id": ticket.formulario_id,
        "prioridade_id": ticket.prioridade_id
    }