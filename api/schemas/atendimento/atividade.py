from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Atividade


class AtividadeSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    processo_id: int = 1
    atividade: str = "Emissão de Nota Fiscal"
    descricao: str = "Emitir uma Nota Fiscal"


class AtividadeViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    processo_id: int = 1
    atividade: str = "Emissão de Nota Fiscal"
    descricao: str = "Emitir uma Nota Fiscal"


class ListagemAtividadesSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    atividades:List[AtividadeSchema]


class AtividadeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class AtividadeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_atividades(atividades: List[Atividade]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for atividade in atividades:
        result.append(
            {
                "id": atividade.id,
                "processo_id": atividade.processo_id,
                "atividade": atividade.atividade,
                "descricao": atividade.descricao
            }
        )
    return {"atividades": result}


def apresenta_atividade(atividade: Atividade):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": atividade.id,
        "processo_id": atividade.processo_id,
        "atividade": atividade.atividade,
        "descricao": atividade.descricao
    }