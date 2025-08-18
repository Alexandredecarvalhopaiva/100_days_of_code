def ganhador(leilao):
    if not leilao:
        print("Não há lances.")
        return None, None

    vencedor = float("-inf")
    nome_vencedor = None

    for nome, valor in leilao.items():
        if valor > vencedor:
            vencedor = valor
            nome_vencedor = nome

    print(f"O ganhador do leilão foi {nome_vencedor}. A proposta vencedora foi R${vencedor:.2f}")
    return nome_vencedor, vencedor


leilao = {}
resposta = ""

while resposta.lower() != "não":
    nome = input("Digite o seu nome: ")
    valor = float(input("Qual é a sua proposta? Dê o seu lance: "))
    leilao[nome] = valor
    print(leilao)
    resposta = input("Deseja inserir outro participante? [sim] ou [não]: \n")
    print("\n" * 100)

ganhador(leilao)