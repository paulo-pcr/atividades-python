'''5- Senha correta: Crie um programa que peça ao usuário para inserir uma senha.
 Enquanto a senha digitada for incorreta, o programa deve continuar pedindo a senha, usando while.'''
senha_correta: str = "1234"

senha_usuario : str = input("Informe a senha:") 


while senha_correta != senha_usuario:
    print("Senha incorreta! Tente novamente.")
    senha_usuario = input("Digite a senha: ")


print("Senha correta! Acesso permitido.")

