'''3- Maior de três números: Desenvolva un programa que receba très números e determine qual é o maior usando if-else.'''
num1 : int = int(input("Digite o primeiro número:"))
num2 : int = int(input("Digite o segundo número: "))
num3 : int = int(input("Digite o terceiro número:"))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é:{num1}")

elif num2 >= num1 and num2>= num3:
    print(f"O maior número é:{num2}")

else:
    print(f"O maior número é:{num3}")
    
