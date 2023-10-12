from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Prioridade

from schemas import *

from logger import logger

prioridade_tag = Tag(name='Prioridade', description='Adição, visualização e atualização de Prioridades')

def configure_prioridade_routes(app: Flask):
    @app.get('/prioridades', tags=[prioridade_tag],
            responses={"200": ListagemPrioridadesSchema, "404": ErrorSchema})
    def get_prioridades():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Prioridades")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        prioridades = session.query(Prioridade).all()

        if not prioridades:
            # se não há projetos cadastrados
            return {"prioridades": []}, 200
        else:
            logger.debug(f"%d Prioridades encontrados" % len(prioridades))
            # retorna a representação do projeto
            return apresenta_prioridades(prioridades), 200
        

    @app.get('/prioridade', tags=[prioridade_tag],
         responses={"200": PrioridadeViewSchema, "404": ErrorSchema})
    def get_prioridade(query: PrioridadeBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        prioridade_id = query.id
        logger.info(f"Coletando dados sobre o Prioridade #{prioridade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        prioridade = session.query(Prioridade).filter(Prioridade.id == prioridade_id).first()

        if not prioridade:
            # se o produto não foi encontrado
            error_msg = "Prioridade não encontrado na base"
            logger.warning(f"Erro ao buscar o Prioridade '{prioridade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Prioridade econtrado: %s" % prioridade)
            # retorna a representação de produto
            return apresenta_prioridade(prioridade), 200


    @app.post('/prioridade', tags=[prioridade_tag],
            responses={"200": PrioridadeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_prioridade(form: PrioridadeSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        prioridade = Prioridade(
            nome=form.nome,
            usuario=form.usuario,
            email=form.email
            )
        logger.debug(f"Adicionando o prioridade '{prioridade.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(prioridade)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{prioridade.nome} adicionado com sucesso.")
            return apresenta_prioridade(prioridade), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o prioridade"
            logger.warning(f"Erro ao adicionar o prioridade '{prioridade.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/prioridade', tags=[prioridade_tag],
                responses={"200": PrioridadeViewSchema, "404": ErrorSchema})
    def put_prioridade(query: PrioridadeBuscaSchema, form: PrioridadeSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        prioridade_id = query.id
        logger.debug(f"Coletando dados sobre o Prioridade #{prioridade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        prioridade = session.query(Prioridade).filter(Prioridade.id == prioridade_id).first()

        if not prioridade:
            # se o carro não foi encontrado
            error_msg = "Prioridade não encontrado na base"
            logger.warning(f"Erro ao editar o Prioridade #'{prioridade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Prioridade: %s" % prioridade)
            prioridade.nome=form.nome
            prioridade.usuario=form.usuario
            prioridade.email=form.email
            session.commit()
            return apresenta_prioridade(prioridade), 200


    @app.delete('/prioridade', tags=[prioridade_tag],
                responses={"200": PrioridadeDelSchema, "404": ErrorSchema})
    def del_prioridade(query: PrioridadeBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        prioridade_id = query.id
        logger.debug(f"Deletando dados sobre prioridade #{prioridade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Prioridade).filter(Prioridade.id == prioridade_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Prioridade #{prioridade_id}")
            return {"mesage": "Prioridade removido", "id": prioridade_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Prioridade não encontrado na base"
            logger.warning(f"Erro ao deletar o Prioridade #'{prioridade_id}', {error_msg}")
            return {"mesage": error_msg}, 404