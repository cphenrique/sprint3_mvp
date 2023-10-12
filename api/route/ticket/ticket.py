from flask import Flask
from flask_openapi3 import Tag

from model import Session
from model import Ticket

from schemas import *

from logger import logger

ticket_tag = Tag(name='Ticket', description='Adição, visualização e atualização de Tickets')

def configure_ticket_routes(app: Flask):
    @app.get('/tickets', tags=[ticket_tag],
            responses={"200": ListagemTicketsSchema, "404": ErrorSchema})
    def get_tickets():
        """ Faz a busca por todos os Projetos cadastrados na base de dados.

        Retorna para uma representação dos projetos.
        """
        logger.debug(f"Coletando Tickets")
        # criando conexão com a base de dados
        session = Session()
        # realizando a busca
        tickets = session.query(Ticket).all()

        if not tickets:
            # se não há projetos cadastrados
            return {"tickets": []}, 200
        else:
            logger.debug(f"%d Tickets encontrados" % len(tickets))
            # retorna a representação do projeto
            return apresenta_tickets(tickets), 200
        

    @app.get('/ticket', tags=[ticket_tag],
         responses={"200": TicketViewSchema, "404": ErrorSchema})
    def get_ticket(query: TicketBuscaSchema):
        """Faz a busca por um Produto a partir do id do produto

        Retorna uma representação dos produtos e comentários associados.
        """
        ticket_id = query.id
        logger.info(f"Coletando dados sobre o Ticket #{ticket_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()

        if not ticket:
            # se o produto não foi encontrado
            error_msg = "Ticket não encontrado na base"
            logger.warning(f"Erro ao buscar o Ticket '{ticket_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            logger.info("Ticket econtrado: %s" % ticket)
            # retorna a representação de produto
            return apresenta_ticket(ticket), 200


    @app.post('/ticket', tags=[ticket_tag],
            responses={"200": TicketViewSchema, "409": ErrorSchema, "400": ErrorSchema})
    def add_ticket(form: TicketSchema):
        """ Adiciona um novo projeto a base de dados.

        Retorna para uma representação dos projetos e atividades relacionadas.
        """
        ticket = Ticket(
            nome=form.nome,
            usuario=form.usuario,
            email=form.email
            )
        logger.debug(f"Adicionando o ticket '{ticket.nome} na base de dados")
        try:
            # criando conexão com a base de dados
            session = Session()
            # adicionando projeto
            session.add(ticket)
            # efetivando o comando de add novo item na tabela
            session.commit()
            logger.debug(f"{ticket.nome} adicionado com sucesso.")
            return apresenta_ticket(ticket), 200
        
        except Exception as e:
            # tratamento de erros
            error_msg = "Não foi possível adicionar o ticket"
            logger.warning(f"Erro ao adicionar o ticket '{ticket.nome}', {error_msg}")
            return {"message": error_msg}, 400


    @app.put('/ticket', tags=[ticket_tag],
                responses={"200": TicketViewSchema, "404": ErrorSchema})
    def put_ticket(query: TicketBuscaSchema, form: TicketSchema):
        """Edita um Carro a partir do id do carro informado

        Retorna uma mensagem de confirmação da remoção.
        """
        ticket_id = query.id
        logger.debug(f"Coletando dados sobre o Ticket #{ticket_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()

        if not ticket:
            # se o carro não foi encontrado
            error_msg = "Ticket não encontrado na base"
            logger.warning(f"Erro ao editar o Ticket #'{ticket_id}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            # edita o carro e retorna a representação
            logger.info("Alterando informações do Ticket: %s" % ticket)
            ticket.nome=form.nome
            ticket.usuario=form.usuario
            ticket.email=form.email
            session.commit()
            return apresenta_ticket(ticket), 200


    @app.delete('/ticket', tags=[ticket_tag],
                responses={"200": TicketDelSchema, "404": ErrorSchema})
    def del_ticket(query: TicketBuscaSchema):
        """Deleta um Projeto a partir do nome do projeto informado

        Retorna uma mensagem de confirmação da remoção.
        """
        ticket_id = query.id
        logger.debug(f"Deletando dados sobre ticket #{ticket_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Ticket).filter(Ticket.id == ticket_id).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            logger.debug(f"Deletado o Ticket #{ticket_id}")
            return {"mesage": "Ticket removido", "id": ticket_id}
        else:
            # se o projeto não foi encontrado
            error_msg = "Ticket não encontrado na base"
            logger.warning(f"Erro ao deletar o Ticket #'{ticket_id}', {error_msg}")
            return {"mesage": error_msg}, 404