from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Atividade

from schemas import *

from logger import logger

atividade_tag = Tag(name='Atividade', description='Adição, visualização e remoção de Atividade')

def configure_atividade_routes(app: Flask):
    @app.get('/atividades', tags=[atividade_tag],
            responses={"200": ListagemAtividadesSchema, "404": ErrorSchema})
    def get_atividades():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Atividades")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        atividades = session.query(Atividade).all()

        if not atividades:
            # se não há projetos cadastrados
            return {"atividades": []}, 200
        else:
            logger.debug(f"%d Atividades encontrados" % len(atividades))
            # retorna a representação do projeto
            return apresenta_atividades(atividades), 200


    @app.get('/atividade', tags=[atividade_tag],
            responses={"200": AtividadeViewSchema, "404": ErrorSchema})
    def get_atividade(query: AtividadeBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        atividade_id = query.id
        logger.info(f"Coletando dados sobre o Atividade #{atividade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        atividade = session.query(Atividade).filter(Atividade.id == atividade_id).first()

        if not atividade:
            # se o produto não foi encontrado
            error_msg = "Atividade não encontrado na base"
            logger.warning(f"Erro ao buscar o Atividade '{atividade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Atividade econtrado: %s" % atividade)
            # retorna a representação de produto
            return apresenta_atividade(atividade), 200


    @app.post('/atividade', tags=[atividade_tag],
            responses={"200": AtividadeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_atividade(form: AtividadeSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        atividade = Atividade(
            nome=form.nome,
            descricao=form.descricao
            )
        logger.debug(f"Adicionando o atividade '{atividade.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(atividade)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{atividade.nome} adicionado com sucesso.")
            return apresenta_atividade(atividade), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o atividade"
            logger.warning(f"Erro ao adicionar o atividade '{atividade.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/atividade', tags=[atividade_tag],
                responses={"200": AtividadeViewSchema, "404": ErrorSchema})
    def put_atividade(query: AtividadeBuscaSchema, form: AtividadeSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        atividade_id = query.id
        logger.debug(f"Coletando dados sobre o Atividade #{atividade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        atividade = session.query(Atividade).filter(Atividade.id == atividade_id).first()

        if not atividade:
            # se o carro não foi encontrado
            error_msg = "Atividade não encontrado na base"
            logger.warning(f"Erro ao editar o Atividade #'{atividade_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Atividade: %s" % atividade)
            atividade.nome=form.nome
            atividade.descricao=form.descricao
            session.commit()
            return apresenta_atividade(atividade), 200


    @app.delete('/atividade', tags=[atividade_tag],
                responses={"200": AtividadeDelSchema, "404": ErrorSchema})
    def del_atividade(query: AtividadeBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        atividade_id = query.id
        logger.debug(f"Deletando dados sobre atividade #{atividade_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Atividade).filter(Atividade.id == atividade_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Atividade #{atividade_id}")
            return {"mesage": "Atividade removido", "id": atividade_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Atividade não encontrado na base"
            logger.warning(f"Erro ao deletar o Atividade #'{atividade_id}', {error_msg}")
            return {"mesage": error_msg}, 404