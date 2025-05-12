'''12- Faça um programa que leia dois números e efetua a adição. Se o valor somado for
maior que 20, este deverá ser apresentado somando-se a ele 8; se o valor somado for
menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

num1 : int = int(input("Digite um número:"))
num2 : int = int(input("Digite mais um número:"))
total = num1 + num2 
if total>20:
    print("Valor total + 8 é:",total+8)
if total<=20:
    print("Valor tatal -5 é:",total-5)

'''13-  Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor da
compra for menor que 20,00; caso contrário, o lucro será de 30%. Ler o valor do produto e
imprimir o valor da venda (conforme as taxas do enunciado).'''

compra: float = float(input("Valor total da compra:"))
if compra < 20:
    lucro = (compra * 45/100) 
    print("Valor da venda :",compra + lucro) 
else:
    lucro = (compra * 30/100) 
    print("Valor da venda :",compra + lucro) 

'''14- Crie um programa com duas variaveis. A variavel A e a variavel B.
 Armazene dois valores em cada uma delas e passe o valor de A para a variavel B.'''

variavel_A : int = 10
variavel_B : int = 20

variavel_A , variavel_B = variavel_B , variavel_A 
print(variavel_A)

    