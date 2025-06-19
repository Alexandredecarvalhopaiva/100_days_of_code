print("Título: As Pedras Perdiadas – A Lenda da Igreja das Três Marias")
print("Você é Alexa, uma arqueólogoa que está em busca de um artefato lendário: a Pedra Angular.")
print("Após dias de viagem, você chegou a uma floresta densa. Dois caminhos se abrem diante de você...")
decisao_1 = input("Para iniciar eu gostaria de entender qual caminho você prefere seguir ?\n 1 - [direita] \n 2 - [esquerda]\n")

ascii_art = """
        ..        ____                                               ____
       . |       / +  \\         ||                       ||         /+ . \\
      .  |       |o x.|        =**=          _          =**=        | o x|
     .   |       |____|         ||         _( )_         ||         |____|
    .    |                      ||        /_____\        ||
   .     |                 ______________//|   |/__________________
  .      |_______^________/                | + |                  /____^_____
 .      .       _U_      /                 |___|                 //   _U_
       .         |      /_______________________________________//     |
      .         /|\\     |______________________________________|/     /|\\
     .   (=========================)     .      . (==========================)
    .    |                         |/|  .       . |                          |
   .     |                         | | .        . |                          |
  .      |_________________________|/|.         . ||------------------------||
     (=========================)  || .          . (==========================|
     |                         |/|  .           . |                          |
     |                         | | .            . |                          |
     |_________________________|/|.             . ||------------------------||
 (=========================)  || .              . (==========================)
 |                         |/|  .               . |                          |
 |                         | | .                . |                          |
 |_________________________|/|.                 . | ________________________ |
 |                        || .                  . ||   -Steve Stewart-      ||
"""
ascii_art2 = r"""
   _____ ____ _____
  /    /      \    \
/____ /_________\____\
\    \          /    /
   \  \        /  /
      \ \    / /
        \ \/ /
          \/
"""


if decisao_1 == "1":
  print("Você seguiu pelo caminho da direita, mas caiu em uma armadilha de caçadores. 🪤")
  print("💀 Fim de jogo.")
if decisao_1 == "2":
  print("Boa escolha! 🌿 Você encontrou uma parte rasgada de um mapa antigo indicando a localização da Pedra Angular.")
  print("Após caminhar mais um pouco, você chega a um rio com correnteza muito forte...")
  decisao_2 = input("O mapa indica que você deve atravessar o rio para chegar a uma ruína sagrada. Você prefere:\n1 - [esperar] pela correnteza baixar\n2 - [atravessar o rio nadando]\nDigite sua escolha: \n")
  if decisao_2 == "2":
    print("A correnteza era forte demais! Você foi arrastado até uma cachoeira e caiu... 💀 Fim de jogo.")
  if decisao_2 == "1":
    print("⏳ Você esperou pacientemente. Algumas horas depois, uma barragem estoura rio acima e a água desaparece!")
    print("Você atravessa o leito seco do rio com facilidade. 🌉")
    print("Você se depara com a velha Igreja das Três Marias, em ruínas...")
    print(ascii_art)
    decisao_3 = input("Dentro da igreja, você vê três caminhos:\n1 - Entrar na sala do sacerdote\n2 - Subir as escadas para o coro\n3 - Explorar um alçapão aberto sob o altar\nDigite 1, 2 ou 3: \n")
    if decisao_3 == "1" or decisao_3 == "2":
      print("Assim que entra, a estrutura frágil da igreja desmorona sobre você. Fim de jogo.")
    if decisao_3 == "3" :
      print("🔎 Você desce pelo alçapão e encontra uma câmara secreta.")
      print("💎 No centro da sala, envolta por runas antigas, está a **Pedra Angular** – brilhando com energia ancestral.")
      print("Parabéns! Você encontrou a primeira das Pedras Perdiadas! Mas cuidado, a estrutura está prestes a ruir...")


      print(ascii_art2)


else:
    print("Escolha inválida. Reinicie o jogo.")