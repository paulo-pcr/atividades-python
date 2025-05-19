'''7- Tabuada de um número: Desenvolva um programa que receba um número e exiba sua tabuada de 1 a 10 usando while.'''
num: int = int(input("Digite um número para ver sua tabuada:"))

contador = 1 

while contador <= 10:
     resultado = num * contador
     print(f"{num} x {contador} = {resultado}")
     contador += 1




 