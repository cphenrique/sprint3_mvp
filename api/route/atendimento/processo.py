from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Processo

from schemas import *

from logger import logger

processo_tag = Tag(name='Processo', description='Adição, visualização e remoção de Processos')

def configure_processo_routes(app: Flask):
    @app.get('/processos', tags=[processo_tag],
            responses={"200": ListagemProcessosSchema, "404": ErrorSchema})
    def get_processos():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Processos")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        processos = session.query(Processo).all()

        if not processos:
            # se não há projetos cadastrados
            return {"processos": []}, 200
        else:
            logger.debug(f"%d Processos encontrados" % len(processos))
            # retorna a representação do projeto
            return apresenta_processos(processos), 200


    @app.get('/processo', tags=[processo_tag],
            responses={"200": ProcessoViewSchema, "404": ErrorSchema})
    def get_processo(query: ProcessoBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        processo_id = query.id
        logger.info(f"Coletando dados sobre o Processo #{processo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        processo = session.query(Processo).filter(Processo.id == processo_id).first()

        if not processo:
            # se o produto não foi encontrado
            error_msg = "Processo não encontrado na base"
            logger.warning(f"Erro ao buscar o Processo '{processo_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Processo econtrado: %s" % processo)
            # retorna a representação de produto
            return apresenta_processo(processo), 200


    @app.post('/processo', tags=[processo_tag],
            responses={"200": ProcessoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_processo(form: ProcessoSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        processo = Processo(
            nome=form.nome,
            descricao=form.descricao
            )
        logger.debug(f"Adicionando o processo '{processo.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(processo)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{processo.nome} adicionado com sucesso.")
            return apresenta_processo(processo), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o processo"
            logger.warning(f"Erro ao adicionar o processo '{processo.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/processo', tags=[processo_tag],
                responses={"200": ProcessoViewSchema, "404": ErrorSchema})
    def put_processo(query: ProcessoBuscaSchema, form: ProcessoSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        processo_id = query.id
        logger.debug(f"Coletando dados sobre o Processo #{processo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        processo = session.query(Processo).filter(Processo.id == processo_id).first()

        if not processo:
            # se o carro não foi encontrado
            error_msg = "Processo não encontrado na base"
            logger.warning(f"Erro ao editar o Processo #'{processo_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Processo: %s" % processo)
            processo.nome=form.nome
            processo.usuario=form.usuario
            processo.email=form.email
            session.commit()
            return apresenta_processo(processo), 200


    @app.delete('/processo', tags=[processo_tag],
                responses={"200": ProcessoDelSchema, "404": ErrorSchema})
    def del_processo(query: ProcessoBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        processo_id = query.id
        logger.debug(f"Deletando dados sobre processo #{processo_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Processo).filter(Processo.id == processo_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Processo #{processo_id}")
            return {"mesage": "Processo removido", "id": processo_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Processo não encontrado na base"
            logger.warning(f"Erro ao deletar o Processo #'{processo_id}', {error_msg}")
            return {"mesage": error_msg}, 404