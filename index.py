from criar_conta import criar
from entrar import entrar
from inicio_do_banco import menu_banco

print('-' * 30)
print('Seu banco'.center(30))
print('-' * 30)
print('Seja bem-vindo ao seu banco!\n'.center(30))

while True:
    print('-' * 30)
    entrar_ou_criar = input('1 - Entrar\n2 - Criar sua conta\n3 - Sair\n' + '-' * 30 + '\n').strip()
    
    if entrar_ou_criar == '1' or entrar_ou_criar == '2' or entrar_ou_criar == '3':
        if entrar_ou_criar == '1':
            cpf_logado = entrar()
            if cpf_logado:
                menu_banco(cpf_logado)
        elif entrar_ou_criar == '2':
            criar()
        elif entrar_ou_criar == '3':
            print('-' * 30)
            sair = input('Deseja realmente sair?\n1 - Sim\n2 - Não \n')
            print('-' * 30)
            if sair == '1':
                print('Até logo!')
                break
            elif sair == '2':
                continue
            else:
                print('Opção inválida. Tente novamente!')
    else:
        print('Opção inválida. Tente novamente.\n')
