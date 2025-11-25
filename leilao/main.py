import art
import function

leilao = {}
resposta = ""

art.art1()

while resposta.lower() != "não":
    nome = input("Digite o seu nome: ")
    valor = float(input("Qual é a sua proposta? Dê o seu lance: "))
    leilao[nome] = valor
    print(leilao)
    resposta = input("Deseja inserir outro participante? [sim] ou [não]: \n")
    print("\n" * 20)

function.ganhador(leilao)