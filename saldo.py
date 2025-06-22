def saldo(cpf_usuario):
    saldo_usuario = 0

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) >= 4 and dados[0] == cpf_usuario:
                    saldo_usuario = float(dados[3])
    except FileNotFoundError:
        pass
    print('-' * 30)
    print(f'Neste momento, Você tem R${saldo_usuario:.2f} no seu saldo')