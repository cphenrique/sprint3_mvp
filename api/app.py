from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session
from model import Analista, Processo, Atividade

from schemas import *

from logger import logger

from flask_cors import CORS

info = Info(title="Tickets de CSC", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
analista_tag = Tag(name='Analista', description='Adição, visualização e remoção de Analistas')
processo_tag = Tag(name='Processo', description='Adição, visualização e remoção de Processos')
atividade_tag = Tag(name='Atividade', description='Adição, visualização e remoção de Atividade')


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha o estilo de documentação.
    """
    return redirect('/openapi/swagger')


@app.get('/analistas', tags=[analista_tag],
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


@app.get('/analista', tags=[analista_tag],
         responses={"200": AnalistaViewSchema, "404": ErrorSchema})
def get_analista(query: AnalistaBuscaPorIDSchema):
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


@app.post('/analista', tags=[analista_tag],
          responses={"200": AnalistaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_analista(form: AnalistaSchema):
    """ Adiciona um novo projeto a base de dados.

    Retorna para uma representação dos projetos e atividades relacionadas.
    """
    analista = Analista(
        nome=form.nome,
        usuario=form.usuario,
        email=form.email
        )
    logger.debug(f"Adicionando o analista '{analista.nome} na base de dados")
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


@app.put('/analista', tags=[analista_tag],
            responses={"200": AnalistaViewSchema, "404": ErrorSchema})
def put_analista(query: AnalistaBuscaSchema, form: AnalistaSchema):
    """Edita um Carro a partir do id do carro informado

    Retorna uma mensagem de confirmação da remoção.
    """
    analista_id = query.id
    logger.debug(f"Coletando dados sobre o Analista #{analista_id}")
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
        analista.usuario=form.usuario
        analista.email=form.email
        session.commit()
        return apresenta_analista(analista), 200


@app.delete('/analista', tags=[analista_tag],
            responses={"200": AnalistaDelSchema, "404": ErrorSchema})
def del_analista(query: AnalistaBuscaSchema):
    """Deleta um Projeto a partir do nome do projeto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    analista_id = query.id
    logger.debug(f"Deletando dados sobre analista #{analista_id}")
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

#==========================================================================================================================

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
def get_processo(query: ProcessoBuscaPorIDSchema):
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
    
#==========================================================================================================================


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
def get_atividade(query: AtividadeBuscaPorIDSchema):
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