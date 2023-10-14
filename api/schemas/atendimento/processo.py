from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Processo


class ProcessoSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    processo: str = "Nota Fiscal"
    descricao: str = "Atividades de emissão, registro e contabilização de Notas Fiscais"


class ProcessoViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    processo: str = "Nota Fiscal"
    descricao: str = "Atividades de emissão, registro e contabilização de Notas Fiscais"


class ListagemProcessosSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    processos:List[ProcessoSchema]


class ProcessoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class ProcessoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_processos(processos: List[Processo]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for processo in processos:
        result.append(
            {
                "id": processo.id,
                "processo": processo.processo,
                "descricao": processo.descricao,
                "atividades": [[a.id, a.atividade] for a in processo.atividades]
            }
        )
    return {"processos": result}


def apresenta_processo(processo: Processo):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": processo.id,
        "processo": processo.processo,
        "descricao": processo.descricao,
        "atividades": [a.atividade for a in processo.atividades]
    }