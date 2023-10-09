from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Unidade


class UnidadeSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Unidade"
    descricao: str = "Breve descrição da unidade."
    logo: str = "logotipo da unidade"
    cor: str = "cor principal"
    acento: str = "cor de acentuação"


class UnidadeViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Unidade"
    descricao: str = "Breve descrição da unidade."
    logo: str = "logotipo da unidade"
    cor: str = "cor principal"
    acento: str = "cor de acentuação"


class ListagemUnidadesSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    unidades:List[UnidadeSchema]


class UnidadeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class UnidadeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_unidades(unidades: List[Unidade]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for unidade in unidades:
        result.append(
            {
                "id": unidade.id,
                "nome": unidade.nome,
                "descricao": unidade.descricao,
                "logo": unidade.logo,
                "cor": unidade.cor,
                "acento": unidade.acento
            }
        )
    return {"unidades": result}


def apresenta_unidade(unidade: Unidade):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": unidade.id,
        "nome": unidade.nome,
        "descricao": unidade.descricao,
        "logo": unidade.logo,
        "cor": unidade.cor,
        "acento": unidade.acento
    }