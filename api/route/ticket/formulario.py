from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Formulario

from schemas import *

from logger import logger

formulario_tag = Tag(name='Formulario', description='Adição, visualização e atualização de Formulários')

def configure_formulario_routes(app: Flask):
    @app.get('/formularios', tags=[formulario_tag],
            responses={"200": ListagemFormulariosSchema, "404": ErrorSchema})
    def get_formularios():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Formularios")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        formularios = session.query(Formulario).all()

        if not formularios:
            # se não há projetos cadastrados
            return {"formularios": []}, 200
        else:
            logger.debug(f"%d Formularios encontrados" % len(formularios))
            # retorna a representação do projeto
            return apresenta_formularios(formularios), 200
        

    @app.get('/formulario', tags=[formulario_tag],
         responses={"200": FormularioViewSchema, "404": ErrorSchema})
    def get_formulario(query: FormularioBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        formulario_id = query.id
        logger.info(f"Coletando dados sobre o Formulario #{formulario_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        formulario = session.query(Formulario).filter(Formulario.id == formulario_id).first()

        if not formulario:
            # se o produto não foi encontrado
            error_msg = "Formulario não encontrado na base"
            logger.warning(f"Erro ao buscar o Formulario '{formulario_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Formulario econtrado: %s" % formulario)
            # retorna a representação de produto
            return apresenta_formulario(formulario), 200


    @app.post('/formulario', tags=[formulario_tag],
            responses={"200": FormularioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_formulario(form: FormularioSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        formulario = Formulario(
            nome=form.nome,
            usuario=form.usuario,
            email=form.email
            )
        logger.debug(f"Adicionando o formulario '{formulario.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(formulario)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{formulario.nome} adicionado com sucesso.")
            return apresenta_formulario(formulario), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o formulario"
            logger.warning(f"Erro ao adicionar o formulario '{formulario.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/formulario', tags=[formulario_tag],
                responses={"200": FormularioViewSchema, "404": ErrorSchema})
    def put_formulario(query: FormularioBuscaSchema, form: FormularioSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        formulario_id = query.id
        logger.debug(f"Coletando dados sobre o Formulario #{formulario_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        formulario = session.query(Formulario).filter(Formulario.id == formulario_id).first()

        if not formulario:
            # se o carro não foi encontrado
            error_msg = "Formulario não encontrado na base"
            logger.warning(f"Erro ao editar o Formulario #'{formulario_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Formulario: %s" % formulario)
            formulario.nome=form.nome
            formulario.usuario=form.usuario
            formulario.email=form.email
            session.commit()
            return apresenta_formulario(formulario), 200


    @app.delete('/formulario', tags=[formulario_tag],
                responses={"200": FormularioDelSchema, "404": ErrorSchema})
    def del_formulario(query: FormularioBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        formulario_id = query.id
        logger.debug(f"Deletando dados sobre formulario #{formulario_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Formulario).filter(Formulario.id == formulario_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Formulario #{formulario_id}")
            return {"mesage": "Formulario removido", "id": formulario_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Formulario não encontrado na base"
            logger.warning(f"Erro ao deletar o Formulario #'{formulario_id}', {error_msg}")
            return {"mesage": error_msg}, 404