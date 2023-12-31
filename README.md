# Ticket app

Sistema para abertura de tickets de atendimento para atividades administrativas.

No estágio atual, de MVP, permite a leitura, adição, edição e remoção de analistas responsáveis pelo atendimento dos tickets.


## Tecnologias utilizadas

Python: Linguagem de programação utilizada no back-end;
Flask: Framework web para construção da aplicação;
SQLAlchemy: Biblioteca de Object-Relational Mapping (ORM);
OpenAPI: Para escrever, produzir, consumir e visualizar serviços da API;
HTML: Linguagem de markup do front-end;
Javascript: Linguagem de programação de comportamento que permite a criação de conteúdo dinâmico;
React: Bibliotecas de JavaScript para desenvolvimento de aplicativos web ou para dispositivos móveis.
Postgres: Sistema gerenciador de banco de dados relacional utilizado para persistência dos dados;


## Premissas

Instruções para instalação abaixo, considero que o Python versão 3 está devidamente instalado e que o módulo pip e virtualenv estão configurados.
Docker também é uma premissa para executar o banco de dados Postgres utilizado para persistência dos dados.
NODE.JS é necessário para que o frontend REACT funcione corretamente. 


## Instalação

1. Banco de Dados

É uma instância do SGBD Postgres e é responsável pela persistência dos dados. É o primeiro componente que deve ser executado, uma vez que os outros componentes dependem do banco de dados para correta inicialização.

Baixar uma imagem do SGBD Postgres

```shell
sudo docker pull postgres
```

Criar uma rede que será compartilhada entre os contâiners para comunicação dos dados

```shell
sudo docker network create mynetwork
```

Inicializar um contâiner a partir da imagem baixada previamente.

```shell
sudo docker run --name postgres-container --network mynetwork -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=ticket -p 5432:5432 -d postgres:latest
```

A partir da correta inicializaçao desse container podemos seguir para os próximos componentes. O SGBD é inicializado sem nenhuma estrutura de tabelas, que é criada posteriormente a partir da primeira execução da API com os modelos de dados.


2. API

A API foi desenvolvida em Flask e controla as rotas de leitura, inserção, deleção dos registros no SGBD.

Acessar a pasta api, com os arquivos da API de conexão com o banco de dados.

Construir uma imagem a partir do Dockerfile.

```shell
sudo docker build -t api .
```

Inicializar o container da API.

```shell
sudo docker run -p 5000:5000 --network mynetwork api
```


3. Frontend

O frontend foi desenvolvido em HTML e JavaScript com REACT e é utilizado para visualizar, inserir, atualizar e deletar novos analistas na base de dados.

Acessar a pasta com o front end

```shell
npm install
```

```shell
npm start
```

O frontend deve ser inicializado na sequencia e com acesso ao api.

O arquivo FIGMA base para o frontend segue abaixo

https://www.figma.com/file/TZ5hl8LSrpDuh97PPqQOQ1/Home-Page?type=design&node-id=0%3A1&mode=dev

## Utilização

![Screencast from 2023-12-11 15-59-42(8)](https://github.com/cphenrique/ticket/assets/88631495/a5fe57fd-589e-4a54-ab6f-2ae86759d2b1)

Para o cadastro de novo analista, deve-se preencher os quatro campos no inicio da tabela com as informações de Nome, Sobrenome, Usuário e Email, todos obrigatórios. Na sequência acionar o botão de "Adiciona" para inclusão do analista no banco de dados.

A edição do registro está liberada para os campos de Usuário e Email, necessário clicar na célula que deseja alteração e na sequência acionar o botão "Atualiza".

Para a remoção do registo deve-se acionar o botão "Deleta" respectiva linha que deseja a remoção.
