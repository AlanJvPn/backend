from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import secrets

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciar um conjunto de Tarefas",
    version="1.0.0",
    contact={"name": "Alan Vila Nova", "email": "alanjvpn@gmail.com"},
)

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

minhas_tarefas = {}


class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluida: bool = False


def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, MEU_USUARIO)
    correct_password = secrets.compare_digest(credentials.password, MINHA_SENHA)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/tarefas")
def get_tarefas(
    page: int = 1,
    limit: int = 10,
    sort_by: str = "nome",
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    if page < 1 or limit < 1:
        raise HTTPException(
            status_code=400,
            detail="Valores de página e limite devem ser maiores que zero.",
        )

    if not minhas_tarefas:
        return {"message": "Não há tarefas cadastradas."}
    else:
        # Lógica de Ordenação
        if sort_by == "nome":
            key_func = lambda x: x[1]["nome_tarefa"].lower()
        elif sort_by == "descricao":
            # Ordena pela descrição
            key_func = lambda x: x[1]["descricao_tarefa"].lower()
        elif sort_by == "id":
            # Ordena pelo ID numérico
            key_func = lambda x: int(x[0])
        else:
            raise HTTPException(
                status_code=400,
                detail="Campo de ordenação inválido. Use 'id', 'nome' ou 'descricao'.",
            )

        tarefas_ordenadas = sorted(minhas_tarefas.items(), key=key_func)

        start = (page - 1) * limit
        end = start + limit

        tarefas_paginadas = [
            {
                "id": id_tarefa,
                "nome_tarefa": tarefa_data["nome_tarefa"],
                "descricao_tarefa": tarefa_data["descricao_tarefa"],
                "concluida": tarefa_data["concluida"],
            }
            for id_tarefa, tarefa_data in tarefas_ordenadas[start:end]]

        return {
            "page": page,
            "limit": limit,
            "sort_by": sort_by,
            "total": len(minhas_tarefas),
            "tarefas": tarefas_paginadas,
        }


@app.post("/adicionar")
def post_tarefas(
    id_tarefa: int,
    tarefa: Tarefa,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    if id_tarefa in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa Tarefa já existe.")
    else:
        minhas_tarefas[id_tarefa] = tarefa.dict()
        return {"message": "A Tarefa foi adicionada com sucesso!"}


@app.put("/atualiza/{id_tarefa}")
def put_tarefa(
    id_tarefa: int,
    tarefa: Tarefa,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    if id_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa Tarefa não foi encontrada")
    else:
        minhas_tarefas[id_tarefa] = tarefa.dict()

        return {"message": "As informações da Tarefa foram atualizadas!"}


@app.delete("/deletar/{id_tarefa}")
def delete_tarefa(
    id_tarefa: int, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)
):
    if id_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa Tarefa não foi encontrado")
    else:
        del minhas_tarefas[id_tarefa]

        return {"message": "Sua tarefa foi deletado!"}
