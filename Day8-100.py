#Estudo de Funções com parâmetros

def greet():
    print("Olá, sou Alexandre Paiva, seu atendente virtual.")
    print("Digite um dos motivos do qual vocês está precisando de ajuda")
    print("1- Financeiro 2- Atendimento personalizado 3- Atualização do cadastro")
    
def greet_with_name(name):
    print(f"Olá {name}, sou Alexandre Paiva, seu atendente virtual.")
    print(f"{name}, digite um dos motivos do qual vocês está precisando de ajuda")
    print("Escolha uma das opções1- Financeiro 2- Atendimento personalizado 3- Atualização do cadastro")


greet()
greet_with_name("Angela")