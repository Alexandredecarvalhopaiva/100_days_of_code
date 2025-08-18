# Projeto final: Caesar Cipher

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('🔐 Aqui você pode codificar e descodificar mensagens, utilizando o método de Caesar Cipher')

# Solicita ao usuário o que ele quer fazer
tentativa = 0
escolha = input("O que deseja fazer? Para encriptografar digite 'encode' e para descriptografar digite 'decode':\n ").lower()

while escolha != 'decode' and escolha != 'encode':
    tentativa += 1
    if tentativa > 10:
        print("❗ O texto está inconsistente. Tente novamente mais tarde.")
        break
    escolha = input("Entrada inválida. Por favor, digite 'encode' ou 'decode': ").lower()

# Solicita o texto e o valor de shift
texto = input("Digite sua mensagem:\n ").lower()
shift = int(input("Defina um número para o Shift (deslocamento):\n "))

# Corrige valores muito altos de shift
shift = shift % len(alfabeto)

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alfabeto:
            index_original = alfabeto.index(letter)
            novo_index = (index_original + shift_amount) % 26
            cipher_text += alfabeto[novo_index]
        else:
            cipher_text += letter  # Mantém espaços e pontuação
    print(f"🔒 Mensagem criptografada: {cipher_text}")

def decrypt(original_text, shift_amount):
    decipher_text = ""
    for letter in original_text:
        if letter in alfabeto:
            index_original = alfabeto.index(letter)
            novo_index = (index_original - shift_amount) % 26
            decipher_text += alfabeto[novo_index]
        else:
            decipher_text += letter  # Mantém espaços e pontuação
    print(f"🔓 Mensagem descriptografada: {decipher_text}")

# Chamada da função conforme a escolha do usuário
if escolha == "encode":
    encrypt(original_text=texto, shift_amount=shift)
elif escolha == "decode":
    decrypt(original_text=texto, shift_amount=shift)

