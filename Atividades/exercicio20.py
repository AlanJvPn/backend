# API de Livros

# GET, POST, PUT, DELETE

# GET - Buscar os dados dos livros
# POST - Adicionar novos livros
# Querry String = http://127.0.0.1:8000/adiciona?id_livro=1&titulo_livro=Carlos&autor_livro=Alan&ano_livro=2002
# PUT - Atualizar informações dos livros
# DELETE - Deletar informações dos livros

from fastapi import FastAPI, HTTPException

app = FastAPI()

meus_livros = {}

@app.get("/livros")
def get_livros():
    if not meus_livros:
        return {"message:" "Não existe nenhum livro."}
    else:
        return {"livros": meus_livros}


# ID, nome, autor, ano
@app.post("/adiciona")
def post_livros(id_livro: int,titulo_livro: str,autor_livro: str,ano_livro: int):
    if id_livro in meus_livros:
        raise HTTPException(status_code=400, detail="Esse Livro já existe")
    else:
        meus_livros[id_livro] = {"titulo_livro": titulo_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return {"message": "O livro foi adicionado com sucesso!"}


@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int,titulo_livro: str,autor_livro: str,ano_livro: int):
    meu_livro = meus_livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse Livro não foi encontrado")
    else:
        if titulo_livro:
            meu_livro["titulo_livro"] = titulo_livro
        if autor_livro:
            meu_livro["autor_livro"] = autor_livro
        if ano_livro:
            meu_livro["ano_livro"] = ano_livro
        
        return {"message": "As informações do Livro foram atualizadas!"}


@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meus_livros:
        raise HTTPException(status_code=404, detail="Esse Livro não foi encontrado")
    else:
        del meus_livros[id_livro]
        
        return {"message": "Seu livro foi deletado!"}     
