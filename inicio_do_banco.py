def menu_banco(cpf_logado):
    from saldo import saldo
    from depositar import depositar
    from sacar import sacar
    from pagar import pagar
    from extrato  import extrato

    while True:
        
        print('O que deseja fazer hoje?')
        print('-'*30)
        
        print('1 - Sacar'.ljust(5) + '2 - Depositar'.rjust(24))
        print('3 - Saldo'.ljust(5) + '4 - Pagar'.rjust(20))
        print('5 - Ver extrato'.ljust(5) + '0 - Sair'.rjust(13))
        print('-'*30)
        escolha = (input())

        if escolha == '1':
            sacar(cpf_logado)
        elif escolha == '2':
            depositar(cpf_logado)
        elif escolha == '3':
            saldo(cpf_logado)
        elif escolha == '4':
            pagar(cpf_logado)
        elif escolha == '5':
            extrato(cpf_logado)
        elif escolha == '0':
            break
        else:
            print('Opção invalida')