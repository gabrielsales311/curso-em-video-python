lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Numero adicionado com sucesso')
    else:
        print('Tente novamente')
    continuar = ' '
    while continuar not in 'SN':
        continuar = (str(input('Deseja continuar? [S/N]'))).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Você digitou os numeros {sorted(lista)}')
