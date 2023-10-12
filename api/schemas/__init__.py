from schemas.error import ErrorSchema

from schemas.atendimento.analista import AnalistaSchema, AnalistaViewSchema, ListagemAnalistasSchema, AnalistaDelSchema, AnalistaBuscaSchema, apresenta_analistas, apresenta_analista
from schemas.atendimento.processo import ProcessoSchema, ProcessoViewSchema, ListagemProcessosSchema, ProcessoDelSchema, ProcessoBuscaSchema, apresenta_processos, apresenta_processo
from schemas.atendimento.atividade import AtividadeSchema, AtividadeViewSchema, ListagemAtividadesSchema, AtividadeDelSchema, AtividadeBuscaSchema, apresenta_atividades, apresenta_atividade

from schemas.local.empresa import *
from schemas.local.unidade import *
from schemas.local.area import *

from schemas.ticket.ticket import *
from schemas.ticket.estado import *
from schemas.ticket.prioridade import *
from schemas.ticket.formulario import *
from schemas.ticket.campo import *
from schemas.ticket.valor import *