import random

# Mensagem de boas-vindas
print(" Bem-vindo ao jogo Pedra, Papel e Tesoura! \n")
print("Regras do jogo:")
print("* Você escolhe entre Pedra, Papel ou Tesoura.")
print("* O computador também fará uma escolha aleatória.")
print("* O resultado será decidido assim:")
print("   - Pedra quebra Tesoura ")
print("   - Tesoura corta Papel ")
print("   - Papel embrulha Pedra")
print("\nVamos jogar! Escolha com sabedoria...\n")

# Arte ASCII
pedra = '''\
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
'''
papel = '''\
     _______
---'   ____)____
          ______)
         _______)
         _______)
---.__________)
'''
tesoura = '''\
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = {
    "Pedra": pedra,
    "Papel": papel,
    "Tesoura": tesoura
}

opcoes = ["Pedra", "Papel", "Tesoura"]

# Entrada do jogador
escolha_do_jogador = input("Escolha uma das opções: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura\n")

if escolha_do_jogador not in ["1", "2", "3"]:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
    sys.exit()

escolha_do_jogador = int(escolha_do_jogador)
jogada_jogador = opcoes[escolha_do_jogador - 1]
jogada_pc = random.choice(opcoes)

# Mostra as escolhas com arte
print(f"\nVocê escolheu: {jogada_jogador}")
print(ascii_art[jogada_jogador])
print(f"O computador escolheu: {jogada_pc}")
print(ascii_art[jogada_pc])

# Lógica do jogo
if jogada_jogador == jogada_pc:
    print("\nEmpate técnico!")
elif (jogada_jogador == "Pedra" and jogada_pc == "Tesoura") or \
     (jogada_jogador == "Papel" and jogada_pc == "Pedra") or \
     (jogada_jogador == "Tesoura" and jogada_pc == "Papel"):
    print("\nParabéns, você venceu!! 🎉")
else:
    print("\nVocê perdeu feio... 😞")
