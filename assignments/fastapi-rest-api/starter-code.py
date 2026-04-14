"""
FastAPI Task Management API - Starter Code

Este é um projeto de uma simples API REST para gerenciar tarefas.
Você irá expandir este código adicionando os endpoints necessários.
"""

from fastapi import FastAPI
from pydantic import BaseModel


# TODO: Defina o modelo Pydantic para Task com os campos: id, title, description, completed
class Task(BaseModel):
    pass  # Adicione os campos aqui


# Inicialize a aplicação FastAPI
app = FastAPI(
    title="Task Management API",
    description="Uma API simples para gerenciar tarefas",
    version="1.0.0"
)


# TODO: Crie uma lista para armazenar as tarefas em memória
tasks = []


# TODO: Implemente o endpoint GET /tasks
# Deve retornar todas as tarefas
@app.get("/tasks", tags=["Tasks"])
async def get_tasks():
    """Retorna a lista de todas as tarefas"""
    pass


# TODO: Implemente o endpoint POST /tasks
# Deve aceitar um objeto Task e adicioná-lo à lista
@app.post("/tasks", tags=["Tasks"])
async def create_task(task: Task):
    """Cria uma nova tarefa"""
    pass


# TODO: Implemente o endpoint GET /tasks/{task_id}
# Deve retornar uma tarefa específica por ID
@app.get("/tasks/{task_id}", tags=["Tasks"])
async def get_task(task_id: int):
    """Retorna uma tarefa específica pelo ID"""
    pass


# TODO: Implemente o endpoint PUT /tasks/{task_id}
# Deve atualizar uma tarefa existente
@app.put("/tasks/{task_id}", tags=["Tasks"])
async def update_task(task_id: int, task: Task):
    """Atualiza uma tarefa existente"""
    pass


# TODO: Implemente o endpoint DELETE /tasks/{task_id}
# Deve remover uma tarefa da lista
@app.delete("/tasks/{task_id}", tags=["Tasks"])
async def delete_task(task_id: int):
    """Deleta uma tarefa existente"""
    pass


# Para executar a aplicação:
# 1. Instale FastAPI: pip install fastapi uvicorn
# 2. Execute: uvicorn starter-code:app --reload
# 3. Acesse a documentação em: http://localhost:8000/docs
