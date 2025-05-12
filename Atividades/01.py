'''1 - Para entrar em um sistema o usuário deve informar
a senha padrão: admin@2025. 
Crie um programa que peça o usuário uma senha e verifica se ela é válida, se for deve ser exibido,
"Autenticação Realizada com Sucesso", senão deve exibir: "Senha Inválida!";
'''
senha : str = str (input("Digite sua senha:"))

if senha == "admin@2025":
    print("Autenticação Realizada com Sucesso")
else:
    print("Senha Inválida!")

'''2- Crie um programa que lê o conceito de um aluno na disciplina BCC201
(Introdução à Programação) e imprime seu significado, de acordo com a
tabela abaixo. Caso seja informado um conceito inexistente, deve ser
exibida uma mensagem de erro.
Conceito Significado
A Excelente
B Ótimo
C Bom
D Regular
E Ruim
F Nos vemos de novo ano que vem...
'''
nota : str = str (input("Sua nota é:"))
if nota == "A":
    print("Excelente")
elif nota == "B":
    print("Ótimo")
elif nota == "C":
    print("Bom")
elif nota == "D":
    print("Regular")
elif nota == "E":
    print("Ruim")
elif nota == "F":
    print("Nos vemos de novo ano que vem...")
else: 
    print("Opçao Inválida")