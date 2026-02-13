from fastapi import FastAPI, HTTPException

app = FastAPI()

tarefas = {}

@app.get("/tarefas")
def listar_tarefas():
    if not tarefas:
        return {"message": "Não há tarefas cadastradas."}
    else:
        return {"tarefas": tarefas}
    

# Nome, Descrição e Concluida = False
@app.post("/adicionar")
def adicionar_tarefa(nome:str, descricao:str):
    if nome in tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe")
    else:
        tarefas[nome] = {"descricao": descricao, "concluida": False}
        return {"message": f"Tarefa {nome} adicionada com sucesso!"}


@app.put("/atualizar/{nome}")
def concluir_tarefa(nome:str):
    tarefa = tarefas.get(nome)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada")
    else:
        tarefa["concluida"] = True
        return {"message": f"Tarefa {nome} concluída!"}
    

@app.delete("/deletar/{nome}")
def deletar_tarefa(nome:str):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada")
    else:
        del tarefas[nome]
        return {"message": f"Tarefa {nome} deletada!"}