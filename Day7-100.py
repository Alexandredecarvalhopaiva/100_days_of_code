import random
stages = [ 
    '''
██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██ 
   ██     ██████   ██████       ███ ███  ██ ██   ████             
''',
    '''
  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██║  ██ ║██╔══╝  ██╔══██╗
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝

 +---+  
 |   |
 O   |
/|\  |
/ \  |
     |
======
''',
    '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
======
''',
    '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
======
''',
    '''
 +---+
 |   |
 O   |
/|   |
     |
     |
======
''',
    '''
 +---+
 |   |
 O   |
 |   |
     |
     |
======
''',
    '''
 +---+
 |   |
 O   |
     |
     |
     |
======
''',
    ''' 
 +---+
 |   |
     |
     |
     |
     |
======'''
]

logo = ['''  
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       

         ┌─────────────────────────┐
         │   PREPARE-SE PARA O     │
         │      JOGO DA FORCA      │
         └─────────────────────────┘
''']

word_list = ["Gol", "Palio", "Uno", "Corsa", "Fiesta", "Fox", "Celta", "HB20", "Ka", "Onix",
    "Siena", "Sandero", "Corolla", "Civic", "Cruze", "Voyage", "Logan", "Clio", "Argo", "Mobi",
    "Spin", "Fit", "T-Cross", "Kwid", "Tracker", "Polo", "Virtus", "Toro", "Compass", "Renegade"]

lives = 6
print(logo)
carro_sorteado = random.choice(word_list).lower()
print(carro_sorteado)

placeholder = ""
word_length = len(carro_sorteado)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Primeiro passo: Escolha de uma palavra aleatoriamente de uma lista
game_over = False
correct_letters = []

while not game_over:  
    print(f"Você pode errar {lives} vezes ")
    guess = input("Guess a letter: ").lower()
    print(guess)

    if guess in correct_letters:
        print(f'Você escolheu essa letra: {guess}')

    display = ""

# Segundo passo: O jogador, usuário, escolhe uma letra:
    palavras_carro_sorteado = list(carro_sorteado)
    print(palavras_carro_sorteado)

# Terceiro passo: Verifica se essa letra tem na palavra escolhida pelo computador:
    for letter in  palavras_carro_sorteado:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

#Redução das vidas após 
    if guess not in palavras_carro_sorteado:
        lives -= 1
        print(f"Você escolheu a letra: {guess}, essa letrão não está na plavra sorteada. Você perdeu uma vida")
        if lives == 0:
            game_over = True
            print(f"A palavra escolhida era: '{carro_sorteado}'")
            print(stages[1])

    if "_" not in display:
        game_over = True
        print(stages[0])
