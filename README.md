📚 Livraria FastAPI

📖 Descrição do Projeto

A Livraria FastAPI é uma API REST desenvolvida em Python utilizando o framework FastAPI.

O projeto simula o funcionamento básico de uma livraria online, permitindo:

Cadastro de usuários
Cadastro de livros
Adição de livros ao carrinho
Validação de usuário antes de permitir operações no carrinho

A aplicação segue uma arquitetura modular, separando responsabilidades em:

Models (validação de dados com Pydantic)
Routers (organização das rotas)
Camada de armazenamento em memória
Testes automatizados com pytest

🚀 Funcionalidades

👤 Usuários

Criar usuário
Listar usuários
Validação de existência para operações no carrinho

📚 Livros

Cadastrar livros
Listar livros disponíveis

🛒 Carrinho

Adicionar livro ao carrinho

Criar carrinho automaticamente para o usuário
Permitir adição apenas se:
O usuário estiver cadastrado
O livro existir

🧠 Regras de Negócio

Um usuário precisa estar cadastrado para adicionar itens ao carrinho.
Um livro só pode ser adicionado se estiver previamente cadastrado.
Cada usuário possui um carrinho individual.
O carrinho armazena os IDs dos livros adicionados.

🛠 Tecnologias Utilizadas

Python 3.12
FastAPI
Pydantic v2
Uvicorn
Pytest

🧪 Testes Automatizados

O projeto possui testes utilizando pytest, validando:

Criação de livros
Criação de usuários
Adição de livros ao carrinho
Regras de validação

🏗 Estrutura do Projeto
livraria_fastapi/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   └── routers/
│
├── tests/
├── requirements.txt
└── pytest.ini

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

Prática de desenvolvimento de APIs REST
Organização de código em arquitetura modular
Implementação de regras de negócio
Escrita de testes automatizados
Preparação para futura integração com banco de dados (SQLite ou PostgreSQL)