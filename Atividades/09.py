'''9-  Faça um programa que leia um número, verifique se este número é positivo ou
negativo. Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão
mostre:" Voce digitou um número positivo.'''

numero : int = int(input("Digite um número:"))
if numero > 0 :
    print("Voce digitou um número positivo.") 
if numero < 0 :
    print("Você digitou um numero negativo")

'''10. Faça um programa que leia um número, verifique se este número é positivo, negativo
ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for
positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou zero”.'''

numero : int = int(input("Digite um número:"))
if numero > 0 :
    print("Voce digitou um número positivo.") 
elif numero < 0 :
    print("Você digitou um numero negativo")
elif numero == 0 :
    print("Você digitou zero")


'''11-  Faça um programa que leia a idade de um nadador e classifique-o numa das
seguintes categorias abaixo:
• Adulto (idade >= 18);
• Juvenil (idade >= 14);
• Infantil (idade >=9);
• Mirim (Idade < 9).
'''
idade : int = int(input("Qual sua idade?"))
if idade >= 18:
    print("Adulto")
elif idade>= 14:
    print("Juvenil")
elif idade>=9:
    print("Infantil")
elif idade < 9:
    print("Mirim")


