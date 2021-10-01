# Instalar tbm uvicorn e usar uvicorn main:app --reload
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Rota raiz
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Criar modelo
class Usuario(BaseModel):
    id: int
    email: str
    senha: str


# Criar base de dados
base_de_dados = [
    Usuario(id=1, email='roger@roger.com', senha='roger123'),
    Usuario(id=2, email='teste@teste.com', senha='teste123')
]


# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados


# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if usuario.id == id_usuario:
            return usuario
    return {"Status": 404, "Mensagem": "Usuário não encontrado"}


# Rota insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario
