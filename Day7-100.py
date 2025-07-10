#Iniciando o dia 7 - Hangmen

#Foi feito o fluxograma do desafio da forca : https://app.diagrams.net/?src=about#G1sFgeVLL0P03mNWC3NlRa8bI6wSNFRx5h#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

import random

def substituir_e_mostrar_posicoes(palavra_original, letra_digitada, substituto, estado_atual):
    posicoes = []

    for i, letra in enumerate(palavra_original):
        if letra.lower() == letra_digitada.lower():
            estado_atual[i] = substituto
            posicoes.append(i)

    return estado_atual, posicoes

# Lista de carros
carros = [
    "Gol", "Palio", "Uno", "Corsa", "Fiesta", "Fox", "Celta", "HB20", "Ka", "Onix",
    "Siena", "Sandero", "Corolla", "Civic", "Cruze", "Voyage", "Logan", "Clio", "Argo", "Mobi",
    "Spin", "Fit", "T-Cross", "Kwid", "Tracker", "Polo", "Virtus", "Toro", "Compass", "Renegade"
]

# Sorteando um carro
carro_sorteado = random.choice(carros).lower()
estado_atual = ["_" for _ in carro_sorteado]

print("🎮 Jogo da Forca: Tema = Carros Populares")
print("Palavra:", " ".join(estado_atual))

# Solicita a letra do usuário
escolha_do_usuario = input("Digite uma letra: ").lower()

# Aplica a substituição
estado_atual, posicoes = substituir_e_mostrar_posicoes(
    carro_sorteado, escolha_do_usuario, escolha_do_usuario, estado_atual
)

print("🔁 Resultado após tentativa:")
print("Palavra:", " ".join(estado_atual))
print("Posições substituídas:", posicoes)
print("Palavra secreta era:", carro_sorteado)