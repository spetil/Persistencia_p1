from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd


app = FastAPI()

alunos_df = pd.DataFrame(columns = ["nome", "nota"])

@app.post("/alunos")
def adicionar_aluno(nome: str, nota: float):
    global alunos_df
    aluno_idx = alunos_df.index[alunos_df["nome"]== nome]
#1
    if aluno_idx.empty:
        novo_aluno = {"nome": nome, "nota":nota}
        alunos_df = alunos_df._append(novo_aluno,ignore_index = True)
        return {"menssagem": f"nota do aluno {nome} atualizada com sucesso"}
    else:
        alunos_df.loc[aluno_idx,"nota"] = nota
        return {"menssagem": f"nota do aluno {nome} atualizada com sucesso"}
#2
@app.get("/alunos/{nome}")
def obter_nota(nome:str):
    filtro = alunos_df["nome"] == nome
    aluno = alunos_df[filtro]

    if aluno.empty:
        return {"mensagem": "Aluno não foi registrado"}
    nota_aluno = aluno.to_dict(orient="records")[0]["nota"]
    return{"nome": nome, "nota": nota_aluno}


#3
@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient="records")
