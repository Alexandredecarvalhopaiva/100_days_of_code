import random

'''#Learn for loops, range and code blocks

#For 

fruits = ["Apple","Banana","Peach","Pear"]

for fruit in fruits:
    print(fruit)

#Aula 2 - Funções matemáticas no python


students_score = [150,100,60,800,850,560,500]

print(f"Somatorio das notas dos alunos: {sum(students_score)}")

nota_maxima = 0
for score in students_score:
    if score > nota_maxima:
        nota_maxima = score
print(nota_maxima)

# outro método de fazer isso é assim 

max_score = max(students_score)
print(f"A nota mais alta foi: {max_score}")

#somatório de números até 100
somatorio = 0 
for number in range (1,101):
    somatorio += number
print(f"O somatório dos valores de 1 a 100 é : {somatorio}")


#Desafio do FizzBuzz
FizzBuzz
Você vai escrever um programa que imprime automaticamente a solução do jogo FizzBuzz. Estas são as regras do jogo FizzBuzz:
- Seu programa deve imprimir cada número de 1 a 100 por vez e incluir o número 100.
- Mas quando o número é divisível por 3, em vez de imprimir o número, ele deve imprimir "Fizz".
- Quando o número é divisível por 5, em vez de imprimir o número, ele deve imprimir "Buzz".
- E se o número for divisível por 3 e 5, por exemplo, 15, em vez do número, ele deve imprimir "FizzBuzz""

for n in range(1,101):
    if n%3 == 0 and n%5 ==0:
        n = ("FizzBuzz")
    elif n%3 == 0:
        n = ("Fizz")
    elif n%5 == 0:
        n = ("Buzz")
    print(n)
'''

import random

# Desafio do gerador de senhas
letras = ["a", "B", "c", "D", "e", "F", "g", "H", "i", "J", "k", "L", "m",
          "N", "o", "P", "q", "R", "s", "T", "u", "V", "w", "X", "y", "Z"]

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

caracteres_especiais = ["'", "@", "#", "!", '"', "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
                      "?", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

print("Olá! Vou te ajudar a criar uma senha mais segura. Vamos começar?")

n1 = int(input("Quantas letras você quer na sua senha? "))
n2 = int(input("Quantos números devem compor a sua senha? "))
n3 = int(input("Quantos caracteres especiais você gostaria de incluir? "))

# Gerando a senha
senha = []

for i in range(n1):
    senha.append(random.choice(letras))
for i in range(n2):
    senha.append(random.choice(numeros))
for i in range(n3):
    senha.append(random.choice(caracteres_especiais))

# Embaralhar os caracteres da senha
random.shuffle(senha)

# Juntar a senha como string
senha_final = ''.join(senha)

print(f"Sua senha segura é:{senha_final}")
