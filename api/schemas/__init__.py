from schemas.error import ErrorSchema

from schemas.atendimento.analista import AnalistaSchema, AnalistaViewSchema, ListagemAnalistasSchema, AnalistaDelSchema, AnalistaBuscaSchema, apresenta_analistas, apresenta_analista
from schemas.atendimento.atividade import AtividadeSchema, AtividadeViewSchema, ListagemAtividadesSchema, AtividadeDelSchema, AtividadeBuscaSchema, apresenta_atividades, apresenta_atividade
from schemas.atendimento.processo import *

from schemas.ticket.ticket import *
from schemas.ticket.estado import *
from schemas.ticket.prioridade import *
from schemas.ticket.formulario import *
from schemas.ticket.campo import *
from schemas.ticket.formulario_campo import *
from schemas.ticket.valor import *