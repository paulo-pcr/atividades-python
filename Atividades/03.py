'''3- Crie um programa que descubra se uma figura geométrica é um quadrado ou um retângulo:
Um quadrado possui a base e a altura iguais enquanto um retângulo tem a base e a 
altura em valores diferentes.'''

base : float = float (input("Medida da base:"))
altura : float = float (input("Medida da altura:"))

if base == altura:
    print("Quadrado")
if base != altura:
    print("Retângulo")



'''4- Crie um programa que recebe 2 números e diz qual deles é o maior.'''

num1 : int = int (input("Digite um número:"))
num2 : int = int (input("Digite um segundo número:"))

if num1 > num2:
    print("O primeiro número digitado é maior que o segundo")
if num1 < num2:
    print("O segundo número digitado é maior que o primeiro")

'''5- Um sacolão da desconto de 5 reais para compras acima de 20 reais em maças. Cada maça custa 1.50.
 Crie um programa que receba um número de maças compradas e calcule o valor a pagar.'''

custo : float = 1.50 
desconto : float = 5.00 
quantidade : float = (input("Digite a quantidades de maçãs:"))
total = float(quantidade)* float(custo)

if total > 20:
    print("Valor total é:",total - float(5))
if total <= 20:
    print("Valor total é:",total)
