def pagar(cpf_usuario):
    print('-' * 30)
    valor = int(input("Qual o valor que deseja pagar? "))
    print('-' * 30)
    nome = input('Para quem deseja pagar')
    print('-' * 30)
    linhas = []
    encontrado = False

    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            if len(dados) >= 4 and dados[0].strip() == cpf_usuario.strip():
                saldo_atual = float(dados[3])
                if saldo_atual == 0:
                    print("Sua conta está zerada, não é possível sacar")
                    return
                elif valor <= saldo_atual:
                    saldo_novo = saldo_atual - valor
                    dados[3] = f'{saldo_novo:.2f}'
                    linha = ','.join(dados)
                    encontrado = True
                else:
                    print("Você não tem saldo suficiente para realizar essa operação")
            linhas.append(linha + "\n")

    if encontrado:
        with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        with open("Extrato.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(f"{cpf_usuario},pagamento,{nome},R${valor:.2f}\n")
        print('-' * 30)
        print("Pagamento realizado com sucesso!")
    else:
        print('-' * 30)
        print("Usuário não encontrado!")
        print('-' * 30)