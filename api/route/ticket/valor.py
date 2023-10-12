from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Valor

from schemas import *

from logger import logger

valor_tag = Tag(name='Valor', description='Adição, visualização e atualização de Valores')

def configure_valor_routes(app: Flask):
    @app.get('/valores', tags=[valor_tag],
            responses={"200": ListagemValoresSchema, "404": ErrorSchema})
    def get_valores():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Valores")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        valores = session.query(Valor).all()

        if not valores:
            # se não há projetos cadastrados
            return {"valores": []}, 200
        else:
            logger.debug(f"%d Valores encontrados" % len(valores))
            # retorna a representação do projeto
            return apresenta_valores(valores), 200
        

    @app.get('/valor', tags=[valor_tag],
         responses={"200": ValorViewSchema, "404": ErrorSchema})
    def get_Valor(query: ValorBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        valor_id = query.id
        logger.info(f"Coletando dados sobre o Valor #{valor_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        valor = session.query(Valor).filter(Valor.id == valor_id).first()

        if not valor:
            # se o produto não foi encontrado
            error_msg = "Valor não encontrado na base"
            logger.warning(f"Erro ao buscar o Valor '{valor_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Valor econtrado: %s" % valor)
            # retorna a representação de produto
            return apresenta_valor(valor), 200


    @app.post('/valor', tags=[valor_tag],
            responses={"200": ValorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_valor(form: ValorSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        valor = Valor(
            valor=form.valor
            )
        logger.debug(f"Adicionando o Valor '{valor.valor} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(valor)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{valor.valor} adicionado com sucesso.")
            return apresenta_valor(valor), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o valor"
            logger.warning(f"Erro ao adicionar o Valor '{valor.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/valor', tags=[valor_tag],
                responses={"200": ValorViewSchema, "404": ErrorSchema})
    def put_valor(query: ValorBuscaSchema, form: ValorSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        valor_id = query.id
        logger.debug(f"Coletando dados sobre o Valor #{valor_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        valor = session.query(Valor).filter(Valor.id == valor_id).first()

        if not valor:
            # se o carro não foi encontrado
            error_msg = "Valor não encontrado na base"
            logger.warning(f"Erro ao editar o Valor #'{valor_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Valor: %s" % valor)
            valor.valor=form.valor
            session.commit()
            return apresenta_valor(valor), 200


    @app.delete('/valor', tags=[valor_tag],
                responses={"200": ValorDelSchema, "404": ErrorSchema})
    def del_valor(query: ValorBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        valor_id = query.id
        logger.debug(f"Deletando dados sobre valor #{valor_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Valor).filter(Valor.id == valor_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Valor #{valor_id}")
            return {"mesage": "Valor removido", "id": valor_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Valor não encontrado na base"
            logger.warning(f"Erro ao deletar o Valor #'{valor_id}', {error_msg}")
            return {"mesage": error_msg}, 404