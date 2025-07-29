#Estudo de Funções com parâmetros

def greet():
    print("Olá, sou Alexandre Paiva, seu atendente virtual.")
    print("Digite um dos motivos do qual vocês está precisando de ajuda")
    print("1- Financeiro 2- Atendimento personalizado 3- Atualização do cadastro")
    
def greet_with_name(name):
    print(f"Olá {name}, sou Alexandre Paiva, seu atendente virtual.")
    print(f"{name}, digite um dos motivos do qual vocês está precisando de ajuda")
    print("Escolha uma das opções1- Financeiro 2- Atendimento personalizado 3- Atualização do cadastro")

def life_in_weeks(nome,idade):
    ano_de_nascimento = 2025-idade 
    semanas_de_vida = (90-idade)*365/7
    semanas_de_vida = int(semanas_de_vida)
    print(f"{nome}, você nasceu em: {ano_de_nascimento}")
    print(f"Você tem {semanas_de_vida} semanas de vida")
'''
greet()
greet_with_name("Angela")'''

'''nome = input("Qual é o seu nome ? ")
idade = int(input("Qual a sua idade ? "))
life_in_weeks(nome,idade)'''

#_________________________________________________________
'''Calculadora do Amor
💪 Este é um desafio difícil! 💪 

Você vai escrever uma função chamada calculate_love_score() que testa a compatibilidade entre dois nomes. Para calcular a pontuação de amor entre duas pessoas: 

1. Pegue os nomes das duas pessoas e verifique o número de vezes que as letras da palavra TRUE ocorrem.   

2. Em seguida, verifique o número de vezes que as letras da palavra LOVE ocorrem.   

3. Em seguida, combine esses números para formar um número de 2 dígitos e imprima-o. 

por exemplo

name1 = "Angela Yu" name2 = "Jack Bauer"

T ocorre 0 vezes 

R ocorre 1 vez 

U ocorre 2 vezes 

E ocorre 2 vezes 

Total = 5 

L ocorre 1 vez 

O ocorre 0 vezes 

V ocorre 0 vezes 

E ocorre 2 vezes 

Total = 3 



Pontuação de amor = 53





Exemplo de entrada 

calculate_love_score("Kanye West", "Kim Kardashian")

Exemplo de saída

42


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")'''

#Projeto final: Caesar Cipher

print('Aqui você pode codificar e descodificar mensagens, utilizando o método de Caesar Cipher')
tentativa = 0
escolha = input("O que deseja fazer? Para encriptografar digite 'encode' e para descriptografar digite 'decode': ").lower()

while escolha != 'decode' and escolha != 'encode':
    tentativa += 1
    if tentativa > 2:
        print("O texto está inconsistente. Você só pode digitar 'decode' ou 'encode'.")
        break
    escolha = input("Entrada inválida. Por favor, digite 'encode' ou 'decode': ").lower()

if escolha == "encode":
    msg = input("Escreva sua mensagem: ")
    # aqui você pode colocar a lógica para criptografar a mensagem
elif escolha == "decode":
    msg = input("Escreva a mensagem a ser descriptografada: ")
    # aqui você pode colocar a lógica para descriptografar a mensagem
