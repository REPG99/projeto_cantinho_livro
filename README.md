Sistema de Gestão de Livraria

Descrição do Projeto
O Sistema de Gestão de Livraria é uma aplicação desenvolvida para controlo e gestão de catálogo de livros, preço, autor e estoque. 

Integrantes do Grupo
Caio Luiz — 01516982
Caio Peryandro Tavares — 01756197
David Rodrigues — 01847148
Igor Bernardo — 01846617
Roberto Eugênio Palácios Gomes — 01241270
Ruan Luiz — 01821025
Ciencia da computação - 4º período manhã

Funcionalidades Implementadas
    Modelagem com Objetos: Dados do catálogo e vendas estruturados como objetos JavaScript.
    Controlo de Stock: Atualização automática da quantidade disponível após cada venda.
    Registo de Livros: Função dedicada para adicionar novas obras ao catálogo com geração automática de ID.
    Funções com Responsabilidades Definidas: Lógica dividida em funções limpas e legíveis.

Tecnologias Utilizadas

Python (v3.x)
Django Framework
HTML5 e CSS3
JavaScript
SQLite (Banco de dados padrão do Django)

Instruções

ativa o venv = python -m venv venv
.\venv\Scripts\activate

Instala o Django = pip install django

migra os dados do banco = python manage.py makemigrations
python manage.py migrate

Inicia o servidor local = python manage.py runserver

Exemplos de saidas = Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 04, 2026 - 10:50:00
Django version 5.0, using settings 'projeto_cantinho_livro.settings'
Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Quit the server with CTRL-BREAK.
    
