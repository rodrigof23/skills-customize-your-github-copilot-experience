# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a construir uma API REST moderna e eficiente usando o framework FastAPI. Você vai criar endpoints, trabalhar com modelos de dados, validação de entrada e entender os conceitos fundamentais de uma arquitetura de API.

## 📝 Tasks

### 🛠️ Criação de Endpoints Básicos

#### Descrição
Crie uma API REST básica com FastAPI que implemente operações CRUD (Create, Read, Update, Delete) para gerenciar uma lista de tarefas.

#### Requisitos
O programa completo deve:

- Inicializar uma aplicação FastAPI com pelo menos 5 endpoints (GET, POST, PUT, DELETE).
- Implementar um endpoint GET `/tasks` que retorna todas as tarefas.
- Implementar um endpoint POST `/tasks` que cria uma nova tarefa.
- Implementar um endpoint GET `/tasks/{task_id}` que retorna uma tarefa específica.
- Implementar um endpoint PUT `/tasks/{task_id}` que atualiza uma tarefa existente.
- Implementar um endpoint DELETE `/tasks/{task_id}` que remove uma tarefa.


### 🛠️ Validação de Dados e Modelos Pydantic

#### Descrição
Utilize Pydantic para definir modelos de dados estruturados e implementar validação automática de entrada.

#### Requisitos
O programa completo deve:

- Definir um modelo `Task` com campos como `id`, `title`, `description`, `completed` (usando Pydantic BaseModel).
- Validar tipos de dados automaticamente (strings, booleanos, etc.).
- Retornar mensagens de erro clara e estruturada quando dados inválidos são enviados.
- Usar anotações de tipo (type hints) em todos os endpoints e funções.

### 🛠️ Documentação Automática

#### Descrição
Aproveite a documentação interativa automática que FastAPI fornece nativamente.

#### Requisitos
O programa completo deve:

- A documentação Swagger estar acessível em `/docs`.
- A documentação ReDoc estar acessível em `/redoc`.
- Todos os endpoints incluírem descrições claras e exemplos de respostas.
- Usar docstrings nos endpoints para melhorar a documentação gerada automaticamente.
