'''Uma tabela de uma loja é a seguinte:

Código Produto Valor

100 -Camisa- 120

101 - Saia 220

102 - Calça 180

103 - Vestido-350

104 -Meia -7.50

Crie un programa que de acordo com o código, exibe produto e o valor.'''

produto: str= input("Informe o código:")

match produto:
    case "100":
        print("Camisa R$120,00")
    case "101":
        print("Saia R$220,00")
    case "102":
        print("Calça R$180,00")
    case "103":
        print("Vestido R$350,00")
    case "104":
        ("Meia R$7,50")
    case _:
        print("Opção inválida!")

'''Desafio 1: (Cris uma segunda versão em que o usuário além do código 
Informe também a quantidade e o programa calcula de acordo com o cadigos
 informado e exibe a seguinte messages por exemplo: A compra de 2 Camisa $240.00'''

produtos: str= input("Informe o código do produto:")

quantidade: float= float(input("Informe a quantidade:"))

match produtos:
    case "100":
        print("A compra de",quantidade,"camisa $",quantidade*120)
    case "101":
        print("A compra de",quantidade,"Saia $",quantidade*220)
    case "102":
        print("A compra de",quantidade,"Calça $",quantidade*180)
    case "103":
        print("A compra de",quantidade,"Vestido $",quantidade*350)
    case "104":
        print("A compra de",quantidade,"Meia $",quantidade*7.50)
    case _:
        print("Opção inválida!")


'''Desafio 2: Aplique um desconto de 18% se a compra for maior que R$500.00'''







            
