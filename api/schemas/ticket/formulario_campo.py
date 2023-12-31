from pydantic import BaseModel
from typing import List
from model import FormularioCampo


class FormularioCampoSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    formulario_id: int = 1
    campo_id: int = 1
    indice: int = 1


class FormularioCampoViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    id: int = 1
    formulario_id: int = 1
    campo_id: int = 1
    indice: int = 1


class ListagemFormularioCamposSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    formulario_campos:List[FormularioCampoSchema]


class FormularioCampoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    id: int = 1


class FormularioCampoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_formulario_campos(formulario_campos: List[FormularioCampo]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for formulario_campo in formulario_campos:
        result.append(
            {
                "id": formulario_campo.id,
                "formulario_id": formulario_campo.formularios.formulario_id
                #"formularios": [f.id for f in formulario_campo.formularios],
                #"campos": [c.id for c in formulario_campo.campos]
            }
        )
    return {"formulario_campos": result}


def apresenta_formulario_campo(formulario_campo: FormularioCampo):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": formulario_campo.id,
        "formularios": [f.id for f in formulario_campo.formularios],
        "campos": [c.id for c in formulario_campo.campos]
    }


# def apresenta_formulario_campos(formularios: List[FormularioCampo]):
#     """ Retorna uma representação dos projetos seguindo o schema definido em
#         ProjetoViewSchema
#     """
#     result = []
#     for formulario in formularios:
#         result.append(
#             {
#                 "id": formulario.id,
#                 "formulario_campos": [f.indice for f in formulario.formulario_campos],
#                 "campos": [[f.id, f.campo, f.tipo] for f in formulario.campos]
#             }
#         )
#     return {"formularios": result}