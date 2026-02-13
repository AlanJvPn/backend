
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

minhas_tarefas = {}

class Tarefa(BaseModel):
    nome_tarefa: str 
    descricao_tarefa: str
    concluida: bool = False

@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não há tarefas cadastradas."}
    else:
        return {"Tarefas": minhas_tarefas}
    

@app.post("/adicionar")
def post_tarefas(id_tarefa: int, tarefa: Tarefa):
    if id_tarefa in minhas_tarefas:
        raise HTTPException(status_code=400, detail= "Essa Tarefa já existe.")
    else:
        minhas_tarefas[id_tarefa] = tarefa.dict()
        return {"message": "A Tarefa foi adicionada com sucesso!"}
    

@app.put("/atualiza/{id_tarefa}")
def put_tarefa(id_tarefa: int, tarefa: Tarefa):
    if id_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa Tarefa não foi encontrada")
    else:
        minhas_tarefas[id_tarefa] = tarefa.dict()
        
        return {"message": "As informações da Tarefa foram atualizadas!"}


@app.delete("/deletar/{id_tarefa}")
def delete_tarefa(id_tarefa: int):
    if id_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa Tarefa não foi encontrado")
    else:
        del minhas_tarefas[id_tarefa]
        
        return {"message": "Sua tarefa foi deletado!"}     
