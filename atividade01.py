''' CRIE UM MENU DE OPÇÕES PARA USUÁRIO NAVEGAR NO SISTEMA:
O MENU TEM ÀS SEGUINTES OPÇÕES:
A - VER SALDO; 
B - DEPOSITAR;
C - SACAR;
D - ENCERRAR CONTA;
X - SAIR DO SISTEMA;

CASO O USUÁRIO ESCOLHA UMA OPÇÃO DIFERENTE EXIBA: OPÇÃO INVÁLIDA.
CASO ELE ESCOLHA UMA DAS OPÇÕES CORRETAS, INFORME PARA ELE EM QUAL PARTE DO
SISTEMA ELE ESTÁ:
EXEMPLO: A - SEU SALDO É R$1.000,00 '''

print("MENU DE OPÇÕES:")
print("A - VER SALDO")
print("B - DEPOSITAR")
print("C - SACAR")
print("D - ENCERRAR CONTA")
print("X - SAIR DO SISTEMA")

opcoes: str = input("Informe a opção desejada:")

match opcoes:
    case "A": 
        print("Seu saldo é: R$10000")
    case "B":
        print("Qual valor deseja depositar?")
    case "C": 
        print("Qual valor deseja sacar?")
    case "D":
        print("Sua conta será encerrada")
    case "x":
        print("Tem certeza que deseja sair?")
    case _:
        print("OPÇÃO INVÁLIDA") 
