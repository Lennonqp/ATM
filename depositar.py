def depositar(cpf_usuario):
    print('Aceitamos apenas cédulas')
    print('-' * 30)
    valor = int(input('Qual o valor que deseja depositar? '))
    print('-' * 30)
    linhas = []
    encontrado = False

    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            if len(dados) >= 4 and dados[0].strip() == cpf_usuario.strip():
                saldo_atual = float(dados[3])
                saldo_novo = saldo_atual + valor
                dados[3] = f'{saldo_novo:.2f}'
                linha = ','.join(dados)
                encontrado = True
            linhas.append(linha + "\n")

    if encontrado:
        with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
            print('-' * 30)
        print("Deposito realizado com sucesso!")
        with open("Extrato.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(f"{cpf_usuario},Deposito,,R${valor:.2f}\n")
    else:
        print('-' * 30)
        print("Usuário não encontrado!")
        print('-' * 30)
