# Engenharia de Software e Padrões de Projeto (5º Semestre)

Este repositório contém uma coleção de projetos desenvolvidos durante o 5º semestre da faculdade. Embora a disciplina fosse de "Business Intelligence", o foco prático foi em conceitos avançados de **Engenharia de Software** para a construção de sistemas robustos.

Aqui você encontrará exemplos práticos dos principais Padrões de Projeto (Design Patterns) em Java e uma API RESTful completa desenvolvida com Node.js e TypeScript.

## 🛠️ Tecnologias Principais

* **Java:** Usado para demonstrar os Padrões de Projeto (Design Patterns).
* **Node.js & TypeScript:** Usados para construir a API RESTful.
* **TypeORM:** ORM para a API, gerenciando a conexão com o banco de dados.
* **Python:** Para scripts de automação.

---

## 🚀 Projetos e Conceitos

### 1. Padrões de Projeto (Design Patterns) em Java

Uma coleção de projetos Java, cada um focado em um padrão de projeto específico:

* **Padrão Strategy** (`/AppNavegacaoStrategy`): Demonstração do padrão Strategy através de um aplicativo de navegação. O sistema pode alterar dinamicamente o método de cálculo de rota (ex: `RotaCarro`, `RotaOnibus`, `RotaAPe`) sem alterar o contexto do navegador.
* **Padrão Factory** (`/Logistica`): Demonstração do padrão Factory para criar objetos de transporte. A fábrica (`LogisticaFactory`) decide se deve instanciar um `Caminhao` ou `Aviao` com base na necessidade.
* **Padrão Prototype** (`/pattern.prototype`): Exemplo do padrão Prototype para clonar objetos de "Funcionários", permitindo a criação de novos objetos com base em um modelo existente de forma eficiente.
* **Sistema de Logística Combinado** (`/Sistema de Logística Flexível`): Um projeto mais complexo que combina múltiplos padrões, incluindo **Abstract Factory** (`TransporteFactory`) e **Strategy** (`EstrategiaEntrega`), para gerenciar um sistema de logística flexível.

### 2. API RESTful de Biblioteca (Node.js)

* **API CRUD Biblioteca** (`/CRUD`): Uma API RESTful completa construída com **Node.js, Express e TypeScript**. Ela utiliza **TypeORM** para gerenciar um sistema de biblioteca, com rotas para criar, ler, atualizar e deletar Alunos, Livros e Empréstimos.

### 3. Scripts Python

* **Disparo de Mensagem** (`/Disparar mensagem.py`): Um script utilitário em Python para automatizar o envio de mensagens.
