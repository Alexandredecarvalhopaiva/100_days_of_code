import random

aleatorio_inteiro = random.randint(1,10)
print(aleatorio_inteiro)

states_of_american = ["Delaware","Pennsylvania","New Jersey","Georgia"]
states_of_american.append("João Pessoa")
print(states_of_american)

friends = ["Alexandre","João","Rejane","Wellyngton O.","Diego","Rosendo","Vinicius","Wellyngton M.","Todos"]
sorteio = random.randint(1,9)

if sorteio == 1:
  print(f"Parabéns {friends[0]} você foi o premiado para pagar a conta!")
elif sorteio == 2:
  print(f"Parabéns {friends[1]} você foi o premiado para pagar a conta!")
elif sorteio == 3:
  print(f"Parabéns {friends[2]} você foi o premiada para pagar a conta!")
elif sorteio == 4:
  print(f"Parabéns {friends[3]} você foi o premiado para pagar a conta!")
elif sorteio == 5:
  print(f"Parabéns {friends[4]} você foi o premiado para pagar a conta!")
elif sorteio == 6:
  print(f"Parabéns {friends[5]} você foi o premiado para pagar a conta!")
elif sorteio == 7:
  print(f"Parabéns {friends[6]} você foi o premiado para pagar a conta!")
else:
  print("A conta será dividida por igual !")
#segunda maneira de fazer o exercício

  friends = ["Alexandre", "João", "Rejane", "Wellyngton O.", "Diego", "Rosendo", "Vinicius", "Wellyngton M."]
  sorteio = random.randint(0, 7)

  print(f"Parabéns {friends[sorteio]} você foi o premiado para pagar a conta!")

  print(random.choice(friends))