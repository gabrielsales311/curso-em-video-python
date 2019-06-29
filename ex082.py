listanum = []
pares = []
impares = []
while True:
    listanum.append(int(input('Digite um numero: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for valores in listanum:
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)

print('-=' * 30)
print(f'A lista completa é {listanum}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')