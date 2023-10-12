INSERT INTO public.empresa(
	empresa_id, nome, descricao, logo)
	VALUES (1, 'Empresa', 'Descrição da Empresa', 'Logo');

INSERT INTO public.unidade(
	unidade_id, nome, descricao, logo, cor, acento, empresa_id)
	VALUES (1, 'Unidade', 'Descrição da Unidade', 'Logo', 'Cinza', 'Azul', 1);

INSERT INTO public.area(
	area_id, nome, descricao, unidade_id)
	VALUES (1, 'Área', 'Descrição da Área', 1);

INSERT INTO public.processo(
	processo_id, processo, descricao)
	VALUES (1, 'Nota Fiscal', 'Emissão, registro e contabilização de Notas Fiscais');
	
INSERT INTO public.processo(
	processo_id, processo, descricao)
	VALUES (2, 'Requisição de Compras', 'Criação de Requisição de Compras para serviços e materiais');
	
INSERT INTO public.processo(
	processo_id, processo, descricao)
	VALUES (3, 'Folha de Serviço', 'Criação de Folha de Serviço para registro de serviços terceirizados');

INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (1, 'Emissão de Nota Fiscal', 'Emitir Nota Fiscal', 1);
	
INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (2, 'Registro de Nota Fiscal', 'Registrar Nota Fiscal no Sistema', 1);
	
INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (3, 'Validação de Nota Fiscal', 'Validar recebimento do material que consta na Nota Fiscal', 1);
	
INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (4, 'Criação de Requisição de Compra de Material', 'Criar uma Requisição de Compra de cotação de material', 2);

INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (5, 'Criação de Requisição de Compra de Serviço', 'Criar uma Requisição de Compra de cotação de serviço', 2);
	
INSERT INTO public.atividade(
	atividade_id, atividade, descricao, processo_id)
	VALUES (6, 'Criação de Folha de Serviço', 'Criar uma Folha de Serviço para registro', 3);

INSERT INTO public.analista(
	analista_id, nome, sobrenome, usuario, email, area_id)
	VALUES (1, 'Analista', '01', 'analista1', 'analista1@tckt.com', 1);

INSERT INTO public.analista(
	analista_id, nome, sobrenome, usuario, email, area_id)
	VALUES (2, 'Analista', '02', 'analista2', 'analista2@tckt.com', 1);

INSERT INTO public.analista(
	analista_id, nome, sobrenome, usuario, email, area_id)
	VALUES (3, 'Analista', '03', 'analista3', 'analista3@tckt.com', 1);

INSERT INTO public.analista(
	analista_id, nome, sobrenome, usuario, email, area_id)
	VALUES (4, 'Analista', '04', 'analista4', 'analista4@tckt.com', 1);

INSERT INTO public.analista(
	analista_id, nome, sobrenome, usuario, email, area_id)
	VALUES (5, 'Analista', '05', 'analista5', 'analista5@tckt.com', 1);

INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (3, 1);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (4, 1);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (5, 1);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (1, 2);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (2, 2);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (3, 2);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (4, 2);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (1, 3);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (2, 3);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (3, 3);
	
INSERT INTO public.analista_processo(
	analista_id, processo_id)
	VALUES (4, 3);

INSERT INTO public.estado(
	estado_id, estado)
	VALUES (1, 'Aberto');
	
INSERT INTO public.estado(
	estado_id, estado)
	VALUES (2, 'Em andamento');
	
INSERT INTO public.estado(
	estado_id, estado)
	VALUES (3, 'Concluído');
	
INSERT INTO public.estado(
	estado_id, estado)
	VALUES (4, 'Suspenso');
	
INSERT INTO public.estado(
	estado_id, estado)
	VALUES (5, 'Cancelado');

INSERT INTO public.prioridade(
	prioridade_id, prioridade)
	VALUES (1, 'Urgente');

INSERT INTO public.prioridade(
	prioridade_id, prioridade)
	VALUES (2, 'Alta');

INSERT INTO public.prioridade(
	prioridade_id, prioridade)
	VALUES (3, 'Média');
	
INSERT INTO public.prioridade(
	prioridade_id, prioridade)
	VALUES (4, 'Baixa');

INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (1, 'Observação', 'Texto', 'Observação do ticket');

INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (2, 'Material', 'Texto', 'Material que deve constar na Nota Fiscal');
		
INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (3, 'Nota Fiscal', 'Texto', 'Número da Nota Fiscal');
	
INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (4, 'Código do material', 'Texto', 'Código do material para inclusão na Requisição de Compra');
	
INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (5, 'Descrição do material', 'Texto', 'Descrição do material para inclusão na Requisição de Compra');
	
INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (6, 'Fornecedor', 'Texto', 'Identificação do fornecedor para inclusão na Requisição de Compra');
	
INSERT INTO public.campo(
	campo_id, campo, tipo, descricao)
	VALUES (7, 'Descrição do serviço', 'Texto', 'Descrição do serviço para inclusão na Requisição de Compra');

INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (1, 1);
	
INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (2, 2);
	
INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (3, 3);

INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (4, 4);
	
INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (5, 5);
	
INSERT INTO public.formulario(
	formulario_id, atividade_id)
	VALUES (6, 6);

INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (1, 2, 1);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (1, 1, 2);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (2, 3, 1);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (2, 1, 2);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (3, 3, 1);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (3, 1, 2);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (4, 4, 1);

INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (4, 5, 2);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (4, 6, 3);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (4, 1, 4);

INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (4, 1, 5);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (5, 6, 1);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (5, 7, 2);
	
INSERT INTO public.formulario_campo(
	formulario_id, campo_id, indice)
	VALUES (5, 1, 3);