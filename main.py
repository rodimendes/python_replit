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
jogo = True
rodada = 1
while jogo:
    print("=-"*20)
    print(f"\n               Rodada {rodada}\n")
    print("=-"*20)
    for jogador in jogadores:
        palavra = input(f"{jogador}, é a sua vez de inserir uma palavra com a letra '{letra.upper()}': [Pressione '0' para sair.").capitalize()
        if palavra == "0":
            jogo = False
        while palavra in lista_palavras:
            chance = 3
            palavra = input(f"{jogador}, esta palavra já foi escolhida. Pense em outra. Você só tem {chance} chances de inserir uma palavra com a letra '{letra.upper()}': ").capitalize()
            chance -= 1
            if chance == 0:
                print('Você perdeu.\nFim do jogo!')
                jogo = False
        lista_palavras.append(palavra)
    rodada += 1
print(lista_palavras)

#resolver problema do zero aparecer na lista
#resolver problema do zero nao parar imediatamente
#quando escrever com letra errada, avisar e pedir para repetir