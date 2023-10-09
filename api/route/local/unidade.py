from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Unidade

from schemas import *

from logger import logger

unidade_tag = Tag(name='Unidade', description='Adição, visualização e remoção de Unidades')

def configure_unidade_routes(app: Flask):
    @app.get('/unidades', tags=[unidade_tag],
            responses={"200": ListagemUnidadesSchema, "404": ErrorSchema})
    def get_unidades():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Unidades")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        unidades = session.query(Unidade).all()

        if not unidades:
            # se não há projetos cadastrados
            return {"unidades": []}, 200
        else:
            logger.debug(f"%d Unidades encontradas" % len(unidades))
            # retorna a representação do projeto
            return apresenta_unidades(unidades), 200
        

    @app.get('/unidade', tags=[unidade_tag],
         responses={"200": UnidadeViewSchema, "404": ErrorSchema})
    def get_unidade(query: UnidadeBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        unidade_id = query.id
        logger.info(f"Coletando dados sobre a Unidade #{unidade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        unidade = session.query(Unidade).filter(Unidade.id == unidade_id).first()

        if not unidade:
            # se o produto não foi encontrado
            error_msg = "Unidade não encontrado na base"
            logger.warning(f"Erro ao buscar o Unidade '{unidade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Unidade econtrado: %s" % unidade)
            # retorna a representação de produto
            return apresenta_unidade(unidade), 200


    @app.post('/unidade', tags=[unidade_tag],
            responses={"200": UnidadeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_unidade(form: UnidadeSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        unidade = Unidade(
            nome=form.nome,
            descricao=form.descricao,
            logo=form.logo,
            cor=form.cor,
            acento=form.acento
            )
        logger.debug(f"Adicionando o unidade '{unidade.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(unidade)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{unidade.nome} adicionado com sucesso.")
            return apresenta_unidade(unidade), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o unidade"
            logger.warning(f"Erro ao adicionar o unidade '{unidade.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/unidade', tags=[unidade_tag],
                responses={"200": UnidadeViewSchema, "404": ErrorSchema})
    def put_unidade(query: UnidadeBuscaSchema, form: UnidadeSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        unidade_id = query.id
        logger.debug(f"Coletando dados sobre o Unidade #{unidade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        unidade = session.query(Unidade).filter(Unidade.id == unidade_id).first()

        if not unidade:
            # se o carro não foi encontrado
            error_msg = "Unidade não encontrado na base"
            logger.warning(f"Erro ao editar o Unidade #'{unidade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Unidade: %s" % unidade)
            unidade.nome=form.nome
            unidade.descricao=form.descricao
            unidade.logo=form.logo
            unidade.cor=form.cor
            unidade.acento=form.cor
            session.commit()
            return apresenta_unidade(unidade), 200


    @app.delete('/unidade', tags=[unidade_tag],
                responses={"200": UnidadeDelSchema, "404": ErrorSchema})
    def del_unidade(query: UnidadeBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        unidade_id = query.id
        logger.debug(f"Deletando dados sobre unidade #{unidade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Unidade).filter(Unidade.id == unidade_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Unidade #{unidade_id}")
            return {"mesage": "Unidade removido", "id": unidade_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Unidade não encontrado na base"
            logger.warning(f"Erro ao deletar o Unidade #'{unidade_id}', {error_msg}")
            return {"mesage": error_msg}, 404