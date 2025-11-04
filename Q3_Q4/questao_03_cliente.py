import httpx

BASE_URL = "http://127.0.0.1:8000"

def adicionar_ou_atualizar_aluno(nome, nota):
    url = f"{BASE_URL}/alunos?nome={nome}&nota={nota}"
    resp = httpx.post(url)
    return resp.json()

def obter_nota_aluno(nome):
    resp = httpx.get(f"{BASE_URL}/alunos/{nome}")
    return resp.json()

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    return resp.json()

#teste
def main():
    
    try:
        #lista
        print("\n[TESTE Q04] GET /alunos (Listando todos)")
        print(listar_alunos())

        #add aluno
        print("\n[TESTE Q03] POST /alunos (Adicionando 3 alunos)")
        print(adicionar_ou_atualizar_aluno("Ana", 8.5))
        print(adicionar_ou_atualizar_aluno("Carlos", 7.2))
        print(adicionar_ou_atualizar_aluno("Fernanda", 9.3))

        #lista
        print("\n[TESTE Q04] GET /alunos (Listando todos)")
        print(listar_alunos())

        #get aluno
        print("\n[TESTE Q03] GET /alunos/{nome} (Buscando 'Carlos')")
        print(obter_nota_aluno("Carlos"))

        #atualiza aluno
        print("\n[TESTE Q03] POST /alunos (Atualiza 'Carlos' para 10.0)")
        print(adicionar_ou_atualizar_aluno("Carlos", 10.0))

        #get aluno
        print("\n[TESTE Q03] GET /alunos/{nome} (Buscando 'Carlos' )")
        print(obter_nota_aluno("Carlos"))

        print("\n[TESTE Q03] GET /alunos/{nome} (Buscando aluno 'Zeca')")
        print(obter_nota_aluno("Zeca"))

    except httpx.ConnectError:
        print("\n[ERRO] Não foi possível conectar ao servidor.")
        print(f"Por favor, verifique se o 'questao_03_04.py' está rodando em {BASE_URL}")

if __name__ == "__main__":
    main()