from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Area

from schemas import *

from logger import logger

area_tag = Tag(name='Area', description='Adição, visualização e remoção de Areas')

def configure_area_routes(app: Flask):
    @app.get('/areas', tags=[area_tag],
            responses={"200": ListagemAreasSchema, "404": ErrorSchema})
    def get_areass():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Unidades")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        areas = session.query(Area).all()

        if not areas:
            # se não há projetos cadastrados
            return {"areas": []}, 200
        else:
            logger.debug(f"%d Areas encontradas" % len(areas))
            # retorna a representação do projeto
            return apresenta_areas(areas), 200
        

    @app.get('/area', tags=[area_tag],
         responses={"200": AreaViewSchema, "404": ErrorSchema})
    def get_area(query: AreaBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        area_id = query.id
        logger.info(f"Coletando dados sobre a Área #{area_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        area = session.query(Area).filter(Area.id == area_id).first()

        if not area:
            # se o produto não foi encontrado
            error_msg = "Área não encontrada na base"
            logger.warning(f"Erro ao buscar a Área '{area_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("área econtrada: %s" % area)
            # retorna a representação de produto
            return apresenta_area(area), 200


    @app.post('/area', tags=[area_tag],
            responses={"200": AreaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_area(form: AreaSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        area = Area(
            nome=form.nome,
            descricao=form.descricao
            )
        logger.debug(f"Adicionando a Área '{area.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(area)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{area.nome} adicionada com sucesso.")
            return apresenta_area(area), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar a Área"
            logger.warning(f"Erro ao adicionar a Área '{area.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/area', tags=[area_tag],
                responses={"200": AreaViewSchema, "404": ErrorSchema})
    def put_area(query: AreaBuscaSchema, form: AreaSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        area_id = query.id
        logger.debug(f"Coletando dados sobre a Área #{area_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        area = session.query(Area).filter(Area.id == area_id).first()

        if not area:
            # se o carro não foi encontrado
            error_msg = "Área não encontrado na base"
            logger.warning(f"Erro ao editar o Área #'{area_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações da Área: %s" % area)
            area.nome=form.nome
            area.descricao=form.descricao
            session.commit()
            return apresenta_area(area), 200


    @app.delete('/area', tags=[area_tag],
                responses={"200": AreaDelSchema, "404": ErrorSchema})
    def del_area(query: AreaBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        area_id = query.id
        logger.debug(f"Deletando dados sobre a Área #{area_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Area).filter(Area.id == area_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado a Área #{area_id}")
            return {"mesage": "Área removida", "id": area_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Área não encontrado na base"
            logger.warning(f"Erro ao deletar a Área #'{area_id}', {error_msg}")
            return {"mesage": error_msg}, 404