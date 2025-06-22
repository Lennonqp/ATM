def criar():
    cpf_valido = False

    while not cpf_valido:
        print('-' * 30)
        cpf = input("Digite o CPF: ".strip())
        print('-' * 30)

        if cpf.isalpha():
            print('-' * 30)
            print("CPF invalido")
        elif '-.' in cpf:
            print('-' * 30)
            print('CPF invalido, INFORMAR APENAS NÚMEROS')
        elif len(cpf) != 11:
            print('-' * 30)
            print("CPF invalido")
        else:
            cpf_valido = True

    nome_valido = False
    while not nome_valido:
        print('-' * 30)
        nome = input("Digite o nome completo: ".title())
        print('-' * 30)

        if nome.replace(" ", "").isalpha():
            nome_valido = True
        else:
            print('-' * 30)
            print("Nome inválido")

    senha_valida = False

    while not senha_valida:
        print('-' * 30)
        senha = input("Digite uma senha:\nOBS: A senha deve ter no minimo oito caracteres\nUma letra maiuscula,\nUma letra minuscula\nUm número:  ".strip())
        if len(senha) < 8:
            print('-' * 30)
            print("Senha invalida")
        elif not any(char.isupper() for char in senha):
            print('-' * 30)
            print("Senha invalida")
        elif not any(char.islower() for char in senha):
            print('-' * 30)
            print("Senha invalida")
        elif not any(char.isdigit() for char in senha):
            print('-' * 30)
            print("Senha invalida")
        elif " " in senha:
            print('-' * 30)
            print("Senha invalida")
        else:
            senha_valida = True

    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{cpf},{nome},{senha},0.00\n")
    print('-' * 30)
    print(f"Cadastro realizado com sucesso\nSeja bem vindo {nome}")
    print('-' * 30)
