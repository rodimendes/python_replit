def nomes(quant_jog):
    participantes = []
    for x in range(quant_jog):
        participantes.append(input(f"Digite o nome do {x+1}° participante: "))
    print(f"OK! {participantes} irão jogar.")
    return participantes

def lista(palavra):
    lista_palavras = []
    
num_jogadores = int(input("Quantos jogadores participarão? "))

jogadores = nomes(num_jogadores)

for nomes

# uma palavra por rodada por participante