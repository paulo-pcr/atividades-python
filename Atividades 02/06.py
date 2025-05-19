'''6 Verificação de idade para dirigir:
 Faça um programa que peça a idade do usuário e informe se ele pode tirar carteira de motorista (idade >= 18), usando if-else.'''

idade: int= int(input("Informe sua idade:"))

if idade >= 18 :
    print("Você já pode tirar sua carteira de motorista !!!")

else:
    print("Você ainda não pode tirar carteira de motorista!!!")