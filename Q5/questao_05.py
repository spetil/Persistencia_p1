from bs4 import BeautifulSoup

vitorias_j1 = 0
vitorias_j2 = 0

with open("C:/Users/lucas/OneDrive/Área de Trabalho/persistecia/Prova/Q5/questao_05.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table", {"id": "jogadas"})
rows = table.find_all("tr")

for row in rows[1:]:
    tds = row.find_all("td")
    j1 = tds[0].string.strip()
    j2 = tds[1].string.strip()
    
    if (j1 == "pedra" and j2 == "tesoura"):
        vitorias_j1 += 1
    elif (j1 == "tesoura" and j2 == "papel"):
        vitorias_j1 += 1
    elif (j1 == "papel" and j2 == "pedra"):
        vitorias_j1 += 1

    elif (j2 == "pedra" and j2 == "tesoura"):
        vitorias_j2 += 1
    elif (j2 == "tesoura" and j1 == "papel"):
        vitorias_j2 += 1
    elif (j2 == "papel" and j1 == "pedra"):
        vitorias_j2 += 1

print(f"O Jogador 1 venceu {vitorias_j1} vez(es).")