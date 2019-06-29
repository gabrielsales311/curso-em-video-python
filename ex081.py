listanum = []
while True:
    listanum.append(input('Digite o valor: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Você digitou {len(listanum)} elementos')

listanum.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listanum}')

if 5 in listanum:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista.')