'''6-   Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas.'''
nota1 : float = float(input("Digite primeira nota:"))
nota2 : float = float(input("Digite segunda nota:"))
nota3 : float = float(input("Digite terceira nota:"))

media = nota1+nota2+nota3/3
print("Sua média é:",media)

'''7-  Faça um programa para converter um certo valor em dólar para reais (ver cotação do dia).'''

dolar : float = ("5.65")
reais : float= float(input("Digite um valor em dolar:"))
total = float(dolar)*float(reais)
print("Seu valor em reais é:R$",total)


'''8-  Faça um programa para converter um certo valor em reais para dólares (ver cotação do dia).'''

reais : float = ("0.18")
dolar : float= float(input("Digite um valor em reais:"))
total = float(dolar)*float(reais)
print("Seu valor em dolar é:",total)
