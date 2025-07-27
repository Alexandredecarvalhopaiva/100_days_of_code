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

greet()
greet_with_name("Angela")

nome = input("Qual é o seu nome ? ")
idade = int(input("Qual a sua idade ? "))
life_in_weeks(nome,idade)

#_________________________________________________________


def calcular_pontuação_de_amor ( nome1 , nome2 ):
  # seu código aqui
 
# Chame sua função com valores codificados
calcular_pontuação_de_amor ( "Kanye West" , "Kim Kardashian" ) 