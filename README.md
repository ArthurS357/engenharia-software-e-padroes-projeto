# Engenharia de Software e Padrões de Projeto (BI - 5º Semestre)

Este repositório contém uma coleção de projetos desenvolvidos durante o 5º semestre da faculdade, na disciplina de Business Intelligence. O foco principal foi aplicar conceitos centrais de Engenharia de Software e Padrões de Projeto (Design Patterns) para construir sistemas robustos e escaláveis.

Aqui você encontrará exemplos práticos de padrões em Java e a construção de uma API RESTful completa com Node.js e TypeScript.

## 🛠️ Tecnologias Principais

* **Java:** Usado para demonstrar os Padrões de Projeto (Design Patterns).
* **Node.js & TypeScript:** Usados para construir a API RESTful.
* **TypeORM:** ORM para a API, gerenciando a conexão com o banco de dados.
* **Python:** Para scripts de automação.

---

## 🚀 Projetos e Conceitos

### 1. Padrões de Projeto (Design Patterns) em Java

Uma coleção de projetos Java, cada um focado em um padrão de projeto específico:

* **Padrão Strategy** (`/Padrao-Strategy`): Demonstração do padrão Strategy através de um aplicativo de navegação. O sistema pode alterar dinamicamente o método de cálculo de rota (ex: `RotaCarro`, `RotaOnibus`, `RotaAPe`).
* **Padrão Factory** (`/Padrao-Factory`): Demonstração do padrão Factory para criar objetos de transporte. O sistema decide se deve instanciar um `Caminhao` ou `Aviao` com base na necessidade.
* **Padrão Prototype** (`/Padrao-Prototype`): Exemplo do padrão Prototype para clonar objetos de "Funcionários", permitindo a criação de novos objetos com base em um modelo existente.
* **Sistema de Logística** (`/Sistema-Logistica-Completo`): Um projeto mais complexo que combina múltiplos padrões, incluindo **Factory, Abstract Factory e Strategy**, para gerenciar um sistema de logística flexível.

### 2. API RESTful de Biblioteca (Node.js)

* **API CRUD Biblioteca** (`/API-CRUD-Biblioteca`): Uma API RESTful completa construída com **Node.js, Express e TypeScript**. Ela utiliza **TypeORM** para gerenciar um sistema de biblioteca, com rotas para criar, ler, atualizar e deletar Alunos, Livros e Empréstimos.

### 3. Scripts Python

* **Disparo de Mensagem** (`/Scripts-Python`): Um script utilitário em Python para automatizar o envio de mensagens.
