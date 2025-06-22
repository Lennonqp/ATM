def extrato(cpf_usuario):
    try:
        with open('extrato.txt', 'r', encoding='utf-8') as arquivo:
            encontrou = False
            print('-' * 30)
            print("Extrato")
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) >= 4 and dados[0] == cpf_usuario:
                    tipo = dados[1]
                    nome_destino = dados[2]
                    valor = dados[3]
                    if nome_destino == '':
                        print('-' * 30)
                        print(f'{tipo.capitalize()}.....R${valor}')
                    else:
                        print('-' * 30)
                        print(f'{tipo.capitalize()} para {nome_destino} :R${valor}')
                    encontrou = True
            if not encontrou:
                print('-' * 30)
                print('Nenhum movimento encontrado')
                print('-' * 30)
    except FileNotFoundError:
        print('-' * 30)
        print('Nenhuma movimentação encontrada')
