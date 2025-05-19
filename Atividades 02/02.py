'''2- Contagem regressiva: Crie um programa que peça ao usuário um número e, utilizando while, faça uma contagem regressiva até zero.'''
numero : int = int(input("Digite um número para fazer a contagem regressiva:"))
while numero > 0:
    print(numero)
    numero -= 1 