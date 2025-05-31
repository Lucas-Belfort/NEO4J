# 🎓 Sistema de Recomendação de Cursos com Neo4j

Este projeto implementa um sistema de recomendação de cursos para estudantes universitários, utilizando **banco de dados orientado a grafos com Neo4j**.

## 📌 Objetivo

Recomendar cursos para alunos com base em perfis semelhantes, considerando:
- Idade próxima (±3 anos)
- Mesmo curso
- Histórico de cursos realizados por outros alunos semelhantes

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- [Neo4j Community Edition](https://neo4j.com/download/)
- Biblioteca `neo4j` para Python

---

## 🧪 Pré-requisitos

1. Ter o **Neo4j Desktop ou Server** instalado e rodando localmente.
2. Criar um banco com autenticação habilitada (ex: usuário `neo4j`, senha `1234`).
3. Instalar dependências do Python:

```bash
pip install neo4j
```

---

## 🚀 Como Executar

1. **Inicie o Neo4j** em `bolt://localhost:7687`.
2. **Altere a senha** em `config.py` se necessário.
3. Execute o script principal:

```bash
python main.py
```

Você verá as **recomendações de cursos** no terminal.

---

## ✅ Funcionalidades

- Cadastro de alunos
- Cadastro de cursos
- Registro de cursos realizados
- Geração de recomendações inteligentes

---

## 📦 Exemplo de Saída

```
Recomendações para João:
Curso recomendado: Didática Geral - Área: Pedagogia
```

---

## 👤 Autor

Trabalho acadêmico para a disciplina de Banco de Dados NoSQL.
