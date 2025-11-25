def ano_bissexto(ano):
  if ano % 4 == 0 and ano % 100 != 0:
    print(f"O {ano} é considerado como ano bissexto")
  elif ano % 4 == 0 and ano % 400 == 0:
    print(f"O {ano} é considerado como ano bissexto")
  else:
    print((f"O {ano} não é considerado como ano bissexto"))

resposta = 0
ano = 0
## ano = int(input(f"Digite um ano e eu te direi se ele é bissexto ou não ! \n "))
ano_bissexto(ano)

while resposta != "n":

  ano = int(input(f"Digite um ano e eu te direi se ele é bissexto ou não ! \n "))
  ano_bissexto(ano)
  resposta =str(input(f"Deseja consultar outro ano ? [s] ou [n]")).lower()
