def nomes(quant_jog):
    participantes = []
    for x in range(quant_jog):
        nome = input(f"Digite o nome do {x+1}° participante: ").capitalize()
        participantes.append(nome)
    print(f"OK! {participantes} irão jogar.")
    return participantes

#==============================#   
#Define a quantidade de jogadores
quant_jog = int(input("Quantos jogadores participarão? "))

#Define a letra da rodada
letra = input("Qual a letra desta rodada? ").lower()

#Aciona a função para nomear os jogadores
jogadores = nomes(quant_jog)

#Início do jogo
lista_palavras = []
for jogador in jogadores:
    palavra = input(f"{jogador}, é a sua vez de inserir uma palavra com a letra '{letra.upper()}': ").capitalize()
    lista_palavras.append(palavra)
print(lista_palavras)

# uma palavra por rodada por participante