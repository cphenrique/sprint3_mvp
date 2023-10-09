from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model import Empresa


class EmpresaSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Empresa LTDA."
    descricao: str = "Breve descrição da empresa."
    logo: str = "logotipo da empresa"


class EmpresaViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    nome: str = "Nome da Empresa LTDA."
    descricao: str = "Breve descrição da empresa."
    logo: str = "logotipo da empresa"


class ListagemEmpresasSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    empresas:List[EmpresaSchema]


class EmpresaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class EmpresaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_empresas(empresas: List[Empresa]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for empresa in empresas:
        result.append(
            {
                "id": empresa.id,
                "nome": empresa.nome,
                "descricao": empresa.descricao,
                "logo": empresa.logo
            }
        )
    return {"empresas": result}


def apresenta_empresa(empresa: Empresa):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": empresa.id,
        "nome": empresa.nome,
        "descricao": empresa.descricao,
        "logo": empresa.logo
    }