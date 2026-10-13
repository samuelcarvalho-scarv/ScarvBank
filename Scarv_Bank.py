print('----- Bem vindo(a) ao ScarvBank -----\n')
print('Escolha a opção desejada.')

saldo = 3000.0

while True:
    escolha = input(
        'Opção: \n'
        ' 1 = Saldo da conta. \n'
        ' 2 = Realizar saque. \n'
        ' 3 = Realizar depósito. \n'
        ' 4 = Finalizar atendimento. \n'
    )

    if escolha == '1':
        print(f'\nSeu saldo é de R${saldo:,.2f}\n'.replace(',' , '@').replace('.' ,',').replace('@' , '.'))

    elif escolha == '2':
        try:
            valor_saque = input('Qual valor deseja sacar? \n').replace(',' , '.')
            valor_saque = float(valor_saque)

        except ValueError:
            print('\nERRO! Digite apenas números para saque! \n')
            continue

        if valor_saque <= saldo and valor_saque > 0:
            saldo -= valor_saque
            print(f'\nFoi retirado de sua conta o valor de: R${valor_saque:,.2f}\n'.replace('.' , ','))

        elif valor_saque <= 0:
            print('\nValor INVÁLIDO!\n')

        else:
            print('\nSaldo insuficiente para completar a operação \n')

    elif escolha == '3':
        try:
            valor_deposito = input('Qual valor deseja depositar? \n').replace(',' , '.')
            valor_deposito = float(valor_deposito)

        except ValueError:
            print('\nERRO! Digite apenas números para depósito! \n')
            continue

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'\nFoi depositado em sua conta o valor de: R${valor_deposito:,.2f}\n'.replace('.' , ','))

        else:
            print('\nValor inválido para depósito \n')

    elif escolha == '4':
        print('\nATENDIMENTO FINALIZADO!\n')
        break

    else:
        print('\nERRO! OPÇÃO INVÁLIDA! \n')