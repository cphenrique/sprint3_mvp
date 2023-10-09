from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Empresa

from schemas import *

from logger import logger

empresa_tag = Tag(name='Empresa', description='Adição, visualização e remoção de Empresas')

def configure_empresa_routes(app: Flask):
    @app.get('/empresas', tags=[empresa_tag],
            responses={"200": ListagemEmpresasSchema, "404": ErrorSchema})
    def get_empresas():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Empresas")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        empresas = session.query(Empresa).all()

        if not empresas:
            # se não há projetos cadastrados
            return {"empresas": []}, 200
        else:
            logger.debug(f"%d Empresas encontradas" % len(empresas))
            # retorna a representação do projeto
            return apresenta_empresas(empresas), 200
        

    @app.get('/empresa', tags=[empresa_tag],
         responses={"200": EmpresaViewSchema, "404": ErrorSchema})
    def get_empresa(query: EmpresaBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        empresa_id = query.id
        logger.info(f"Coletando dados sobre a Empresa #{empresa_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        empresa = session.query(Empresa).filter(Empresa.id == empresa_id).first()

        if not empresa:
            # se o produto não foi encontrado
            error_msg = "Empresa não encontrada na base"
            logger.warning(f"Erro ao buscar a Empresa '{empresa_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Empresa econtrada: %s" % empresa)
            # retorna a representação de produto
            return apresenta_empresa(empresa), 200


    @app.post('/empresa', tags=[empresa_tag],
            responses={"200": EmpresaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_empresa(form: EmpresaSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        empresa = Empresa(
            nome=form.nome,
            descricao=form.descricao,
            logo=form.logo
            )
        logger.debug(f"Adicionando a Empresa '{empresa.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(empresa)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{empresa.nome} adicionado com sucesso.")
            return apresenta_empresa(empresa), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar a Empresa"
            logger.warning(f"Erro ao adicionar a Empresa '{empresa.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/empresa', tags=[empresa_tag],
                responses={"200": EmpresaViewSchema, "404": ErrorSchema})
    def put_empresa(query: EmpresaBuscaSchema, form: EmpresaSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        empresa_id = query.id
        logger.debug(f"Coletando dados sobre a Empresa #{empresa_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        empresa = session.query(Empresa).filter(Empresa.id == empresa_id).first()

        if not empresa:
            # se o carro não foi encontrado
            error_msg = "Empresa não encontrada na base"
            logger.warning(f"Erro ao editar a Empresa #'{empresa_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações da Empresa: %s" % empresa)
            empresa.nome=form.nome
            empresa.descricao=form.descricao
            empresa.logo=form.logo
            session.commit()
            return apresenta_empresa(empresa), 200


    @app.delete('/empresa', tags=[empresa_tag],
                responses={"200": EmpresaDelSchema, "404": ErrorSchema})
    def del_empresa(query: EmpresaBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        empresa_id = query.id
        logger.debug(f"Deletando dados sobre a Empresa #{empresa_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Empresa).filter(Empresa.id == empresa_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado a Empresa #{empresa_id}")
            return {"mesage": "Empresa removida", "id": empresa_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Empresa não encontrada na base"
            logger.warning(f"Erro ao deletar a Empresa #'{empresa_id}', {error_msg}")
            return {"mesage": error_msg}, 404