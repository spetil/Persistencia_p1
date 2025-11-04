soma_notas = 0
contador = 0
maior_nota = 0.0
menor_nota = 1000.0  
aluno_maior_nota = ""
aluno_menor_nota = ""

with open("C:/Users/lucas/OneDrive/Área de Trabalho/persistecia/Prova/Q1/dados_alunos.txt", "r") as file:
    linha = file.readline()

    while(linha):
        linha_limpa = linha.strip()
        dados = linha_limpa.split('#')
        nome = dados[0]
        nota = float(dados[2])
        soma_notas += nota
        contador += 1
        
        if nota > maior_nota:
            maior_nota = nota
            aluno_maior_nota = nome
            
        if nota < menor_nota:
            menor_nota = nota
            aluno_menor_nota = nome

        linha = file.readline()

media = soma_notas / contador

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota} ({aluno_maior_nota})")
print(f"Menor nota: {menor_nota} ({aluno_menor_nota})")