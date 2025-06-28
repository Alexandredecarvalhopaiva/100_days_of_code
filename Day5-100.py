#Learn for loops, range and code blocks

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
'''FizzBuzz
Você vai escrever um programa que imprime automaticamente a solução do jogo FizzBuzz. Estas são as regras do jogo FizzBuzz:
- Seu programa deve imprimir cada número de 1 a 100 por vez e incluir o número 100.
- Mas quando o número é divisível por 3, em vez de imprimir o número, ele deve imprimir "Fizz".
- Quando o número é divisível por 5, em vez de imprimir o número, ele deve imprimir "Buzz".
- E se o número for divisível por 3 e 5, por exemplo, 15, em vez do número, ele deve imprimir "FizzBuzz""'''

for n in range(1,101):
    if n%3 == 0:
        n = ("Fizz")
    print(n)