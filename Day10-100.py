def ano_bissexto(ano):
    """Digite o ano e eu te direi se ele é um ano bissexto"""
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

resposta = "s"

while resposta != "n":
    ano = int(input("Digite um ano e eu direi se ele é bissexto: "))
    ano_bissexto(ano)
    resposta = input("Deseja consultar outro ano? [s/n]: ").lower()