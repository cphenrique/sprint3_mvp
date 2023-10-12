from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Campo

from schemas import *

from logger import logger

campo_tag = Tag(name='Campo', description='Adição, visualização e atualização de Campos')

def configure_campo_routes(app: Flask):
    @app.get('/campos', tags=[campo_tag],
            responses={"200": ListagemCamposSchema, "404": ErrorSchema})
    def get_campos():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Campos")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        campos = session.query(Campo).all()

        if not campos:
            # se não há projetos cadastrados
            return {"campos": []}, 200
        else:
            logger.debug(f"%d Campos encontrados" % len(campos))
            # retorna a representação do projeto
            return apresenta_campos(campos), 200
        

    @app.get('/campo', tags=[campo_tag],
         responses={"200": CampoViewSchema, "404": ErrorSchema})
    def get_campo(query: CampoBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        campo_id = query.id
        logger.info(f"Coletando dados sobre o Campo #{campo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        campo = session.query(Campo).filter(Campo.id == campo_id).first()

        if not campo:
            # se o produto não foi encontrado
            error_msg = "Campo não encontrado na base"
            logger.warning(f"Erro ao buscar o Campo '{campo_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Campo econtrado: %s" % campo)
            # retorna a representação de produto
            return apresenta_campo(campo), 200


    @app.post('/campo', tags=[campo_tag],
            responses={"200": CampoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_campo(form: CampoSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        campo = Campo(
            nome=form.nome,
            usuario=form.usuario,
            email=form.email
            )
        logger.debug(f"Adicionando o campo '{campo.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(campo)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{campo.nome} adicionado com sucesso.")
            return apresenta_campo(campo), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o campo"
            logger.warning(f"Erro ao adicionar o campo '{campo.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/campo', tags=[campo_tag],
                responses={"200": CampoViewSchema, "404": ErrorSchema})
    def put_campo(query: CampoBuscaSchema, form: CampoSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        campo_id = query.id
        logger.debug(f"Coletando dados sobre o Campo #{campo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        campo = session.query(Campo).filter(Campo.id == campo_id).first()

        if not campo:
            # se o carro não foi encontrado
            error_msg = "Campo não encontrado na base"
            logger.warning(f"Erro ao editar o Campo #'{campo_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Campo: %s" % campo)
            campo.nome=form.nome
            campo.usuario=form.usuario
            campo.email=form.email
            session.commit()
            return apresenta_campo(campo), 200


    @app.delete('/campo', tags=[campo_tag],
                responses={"200": CampoDelSchema, "404": ErrorSchema})
    def del_campo(query: CampoBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        campo_id = query.id
        logger.debug(f"Deletando dados sobre campo #{campo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Campo).filter(Campo.id == campo_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Campo #{campo_id}")
            return {"mesage": "Campo removido", "id": campo_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Campo não encontrado na base"
            logger.warning(f"Erro ao deletar o Campo #'{campo_id}', {error_msg}")
            return {"mesage": error_msg}, 404