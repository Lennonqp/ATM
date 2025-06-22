def entrar():
    logado = False
    while not logado:
        print('-' * 30)
        login = input("Digite seu login: ").strip()
        print('-' * 30)
        senha = input("Digite sua senha: ").strip()
        print('-' * 30)
        encontrado = False

        try:
            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(",")
                    if len(dados) >= 3:
                        cpf_salvo = dados[0].strip()
                        nome_salvo = dados[1].strip()
                        senha_salva = dados[2].strip()
                        if login == cpf_salvo and senha == senha_salva:
                            print(f"Bem-vindo, {nome_salvo}!")
                            encontrado = True
                            logado = True
                            return cpf_salvo
            if not encontrado:
                print('-' * 30)
                print("CPF ou senha incorretos.")
        except FileNotFoundError:
            print('-' * 30)
            print("Nenhum usuário cadastrado ainda.")
            print('-' * 30)
            return None
