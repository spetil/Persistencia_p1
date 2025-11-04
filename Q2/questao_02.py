import pandas as pd

dados_receitas = [12000, 17500, 14300, 16000, 19500]
associados = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"]

receitas = pd.Series(dados_receitas, index= associados)
#print("-----------------")
#print(receitas)
#print("-----------------")

total_arrecadado = receitas.sum()
print("-Total arrecadado-")
print(total_arrecadado)
print("-----------------")

media_receitas = receitas.mean()
print("-Media da receita-")
print(media_receitas)
print("-----------------")

associado_s = receitas.idxmax()
print("-associado que mais arrecadou-")
print(associado_s)
print("-----------------")

associado_acima = receitas[receitas > media_receitas]
print("\n--- Associados acima da média ---")
print(associado_acima)
