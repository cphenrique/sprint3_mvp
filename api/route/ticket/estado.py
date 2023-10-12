from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Estado

from schemas import *

from logger import logger

estado_tag = Tag(name='Estado', description='Adição, visualização e atualização de Tickets')

def configure_estado_routes(app: Flask):
    @app.get('/estados', tags=[estado_tag],
            responses={"200": ListagemEstadosSchema, "404": ErrorSchema})
    def get_estados():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Estados")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        estados = session.query(Estado).all()

        if not estados:
            # se não há projetos cadastrados
            return {"estados": []}, 200
        else:
            logger.debug(f"%d Estados encontrados" % len(estados))
            # retorna a representação do projeto
            return apresenta_estados(estados), 200
        

    @app.get('/estado', tags=[estado_tag],
         responses={"200": EstadoViewSchema, "404": ErrorSchema})
    def get_estado(query: EstadoBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        estado_id = query.id
        logger.info(f"Coletando dados sobre o Estado #{estado_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        estado = session.query(Estado).filter(Estado.id == estado_id).first()

        if not estado:
            # se o produto não foi encontrado
            error_msg = "Estado não encontrado na base"
            logger.warning(f"Erro ao buscar o Estado '{estado_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Estado econtrado: %s" % estado)
            # retorna a representação de produto
            return apresenta_estado(estado), 200


    @app.post('/estado', tags=[estado_tag],
            responses={"200": EstadoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_estado(form: EstadoSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        estado = Estado(
            estado=form.estado
            )
        logger.debug(f"Adicionando o Estado '{estado.estado} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(estado)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{estado.estado} adicionado com sucesso.")
            return apresenta_estado(estado), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o Estado"
            logger.warning(f"Erro ao adicionar o Estado '{estado.estado}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/estado', tags=[estado_tag],
                responses={"200": EstadoViewSchema, "404": ErrorSchema})
    def put_estado(query: EstadoBuscaSchema, form: EstadoSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        estado_id = query.id
        logger.debug(f"Coletando dados sobre o Estado #{estado_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        estado = session.query(Estado).filter(Estado.id == estado_id).first()

        if not estado:
            # se o carro não foi encontrado
            error_msg = "Estado não encontrado na base"
            logger.warning(f"Erro ao editar o Estado #'{estado_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Estado: %s" % estado)
            estado.estado=form.estado
            session.commit()
            return apresenta_estado(estado), 200


    @app.delete('/estado', tags=[estado_id],
                responses={"200": EstadoDelSchema, "404": ErrorSchema})
    def del_estado(query: EstadoBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        estado_id = query.id
        logger.debug(f"Deletando dados sobre Estado #{estado_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Estado).filter(Estado.id == estado_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Estado #{estado_id}")
            return {"mesage": "Estado removido", "id": estado_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Estado não encontrado na base"
            logger.warning(f"Erro ao deletar o Estado #'{estado_id}', {error_msg}")
            return {"mesage": error_msg}, 404