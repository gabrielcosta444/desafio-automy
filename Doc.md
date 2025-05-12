# Documentação Técnica 

- Nome: Gabriel da Cunha Costa
- CPF: 70134547616
- Email: gabrielcunhacosta2005@hotmail.com
- Número: 31996728646

---

## Visão Geral

Este projeto tem como objetivo disponibilizar um aplicativo web que permite aos clientes de um kartódromo consultarem suas baterias (corridas) previamente agendadas com base em um endereço de e-mail informado.

O sistema realiza autenticação via API, consulta uma base de dados remota e retorna uma resposta estruturada com informações sobre as corridas futuras e passadas.

---

## Como Utilizar o Aplicativo

### Acesso

O aplicativo está disponível por meio de uma interface web. O usuário deve:

1. Acessar a página inicial em um navegador web.
2. Informar o endereço de e-mail no campo apropriado.
3. Clicar no botão "Consultar".
4. Visualizar na tela as próximas baterias agendadas, caso existam.
5. Caso deseje, poderá visualizar as baterias passadas (caso existam) por meio de um botão adicional.

### Interface

- Campo de entrada de e-mail.
- Botão de consulta.
- Área de exibição dos resultados:
  - Baterias futuras.
  - Opção para exibição de baterias passadas.

---

## Funcionalidades

A aplicação é composta por diferentes módulos que se integram para atender ao objetivo proposto.

-O módulo `auth.py` contém a função responsável por autenticar a aplicação na API da Automy, retornando um token JWT necessário para as demais requisições.

-O módulo `query_service.py` realiza a consulta dos dados relacionados às baterias a partir do e-mail informado. Ele utiliza o token de autenticação e monta a query para buscar os registros no banco.

-Em seguida, o módulo `output.py` trata os dados recebidos, separando as baterias futuras das passadas. Ele também formata a resposta para exibição no frontend, gerando mensagens de forma clara para o usuário final.

-O arquivo `app.py` é o servidor principal da aplicação. Ele define as rotas da API e integra os módulos de autenticação.

-No lado do cliente, a aplicação utiliza um frontend simples com HTML, CSS e JavaScript. A página `index.html` é renderizada pelo Flask e oferece a interface de consulta. O script `script.js` é responsável por capturar o e-mail informado, realizar a chamada ao backend e manipular o DOM para exibir a resposta.

---

## Processo de Build e Deploy

### Estrutura de Diretórios

- `raiz/`
  - `src/`
    - `app.py`
    - `auth.py`
    - `query_service.py`
    - `output.py`
    - `templates/`
      - `index.html`
    - `static/`
      - `style.css`
      - `script.js`
  - `Dockerfile`
  - `docker-compose.yaml`
  - `requirements.txt`

### Docker: Build e Execução

1. **Build da imagem:**

   ```bash
   docker-compose build

2. **Inicialização do aplicativo:

   ```bash
   docker-compose up

   




