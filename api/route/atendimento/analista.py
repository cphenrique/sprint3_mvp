from flask import Flask, request
from flask_openapi3 import Tag

from model import Session
from model import Analista

from schemas import *

from logger import logger



analista_tag = Tag(name='Analista', description='Adição, visualização e remoção de Analistas')

def configure_analista_routes(app: Flask):
    @app.get('/get_analistas', tags=[analista_tag],
            responses={"200": ListagemAnalistasSchema, "404": ErrorSchema})
    def get_analistas():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Analistas")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        analistas = session.query(Analista).all()

        if not analistas:
            # se não há projetos cadastrados
            return {"analistas": []}, 200
        else:
            logger.debug(f"%d Analistas encontrados" % len(analistas))
            # retorna a representação do projeto
            return apresenta_analistas(analistas), 200
        

    @app.get('/get_analista', tags=[analista_tag],
         responses={"200": AnalistaViewSchema, "404": ErrorSchema})
    def get_analista(query: AnalistaBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        analista_id = query.id
        logger.info(f"Coletando dados sobre o Analista #{analista_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        analista = session.query(Analista).filter(Analista.id == analista_id).first()

        if not analista:
            # se o produto não foi encontrado
            error_msg = "Analista não encontrado na base"
            logger.warning(f"Erro ao buscar o Analista '{analista_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Analista econtrado: %s" % analista)
            # retorna a representação de produto
            return apresenta_analista(analista), 200


    @app.post('/add_analista', tags=[analista_tag],
            responses={"200": AnalistaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_analista(form: AnalistaSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """

        analista = Analista(
            nome=form.nome,
            sobrenome=form.sobrenome,
            usuario=form.usuario,
            email=form.email
            )

        logger.info(f"Adicionando o analista '{analista.nome}' na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(analista)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{analista.nome} adicionado com sucesso.")
            return apresenta_analista(analista), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o analista"
            logger.warning(f"Erro ao adicionar o analista '{analista.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.post('/add_analista_json', tags=[analista_tag],
            responses={"200": AnalistaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_analista_json(form: AnalistaSchemaJson):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """

        data = request.json
        
        logger.debug(data)
        print(data)
        print('######################')
        
        analista = Analista(
            nome=data.get('nome'),
            sobrenome=data.get('sobrenome'),
            usuario=data.get('usuario'),
            email=data.get('email')
        )

        logger.debug(f"Adicionando o analista '{analista.nome}' na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(analista)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{analista.nome} adicionado com sucesso.")
            return apresenta_analista(analista), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o analista"
            logger.warning(f"Erro ao adicionar o analista '{analista.nome}', {error_msg}")
            return {"message": error_msg}, 400



    @app.put('/put_analista', tags=[analista_tag],
                responses={"200": AnalistaViewSchema, "404": ErrorSchema})
    def put_analista(query: AnalistaBuscaSchema, form: AnalistaSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        analista_id = query.id
        logger.info(f"Coletando dados sobre o Analista #{analista_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        analista = session.query(Analista).filter(Analista.id == analista_id).first()

        if not analista:
            # se o carro não foi encontrado
            error_msg = "Analista não encontrado na base"
            logger.warning(f"Erro ao editar o Analista #'{analista_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Analista: %s" % analista)
            analista.nome=form.nome
            analista.sobrenome=form.sobrenome,
            analista.usuario=form.usuario
            analista.email=form.email
            session.commit()
            return apresenta_analista(analista), 200


    @app.delete('/del_analista', tags=[analista_tag],
                responses={"200": AnalistaDelSchema, "404": ErrorSchema})
    def del_analista(query: AnalistaBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        analista_id = query.id
        logger.info(f"Deletando dados sobre analista #{analista_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Analista).filter(Analista.id == analista_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Analista #{analista_id}")
            return {"mesage": "Analista removido", "id": analista_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Analista não encontrado na base"
            logger.warning(f"Erro ao deletar o Analista #'{analista_id}', {error_msg}")
            return {"mesage": error_msg}, 404