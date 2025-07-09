#Iniciando o dia 7 - Hangmen

#Foi feito o fluxograma do desafio da forca : https://app.diagrams.net/?src=about#G1sFgeVLL0P03mNWC3NlRa8bI6wSNFRx5h#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

import random

carros = ["Gol", "Palio", "Uno", "Corsa", "Fiesta", "Fox", "Celta", "HB20", "Ka", "Onix",
    "Siena", "Sandero", "Corolla", "Civic", "Cruze", "Voyage", "Logan", "Clio", "Argo", "Mobi",
    "Spin", "Fit", "T-Cross", "Kwid", "Tracker", "Polo", "Virtus", "Toro", "Compass", "Renegade"]


carro_sorteado = print(random.choice(carros))
