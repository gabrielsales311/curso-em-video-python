n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opc = int(input('Digite a opção: '))
    if opc == 1:
        print('A soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
    elif opc == 2:
            print('{} vezes {} é {}'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            print("O numero {} é maior que {}".format(n1, n2))
        elif n2 > n1:
            print('O numero {} é maior que {}'.format(n2, n1))
        else:
            print('Os numeros são iguais')
    elif opc == 4:
        n1 = float(input('Digite o novo primeiro numero: '))
        n2 = float(input('Digite o novo segundo numero: '))
    elif opc == 5:
        print('Tchau e obrigado pelos peixes!')
    else:
        print('Opção invalida')
