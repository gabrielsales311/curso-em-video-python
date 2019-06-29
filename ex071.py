valor = int(input('Valor que você quer sacar: '))

while True:
    # Notas de cinquenta
    notascinquenta = valor // 50
    restocinequnta = valor % 50

    # Notas de vinte
    notasvinte = restocinequnta // 20
    restovinte = restocinequnta % 20

    # Notas de dez
    notasdez = restovinte // 10
    restodez = restovinte % 10

    # Notas de um
    notasum = restodez // 1

    if notascinquenta >= 1:
        print(f'Total de {notascinquenta} notas de R$50')
    if notasvinte >= 1:
        print(f'Total de {notasvinte} notas de R$20')
    if notasdez >= 1:
        print(f'Total de {notasdez} notas de R$10')
    if notasum >= 1:
        print(f'Total de {notasum} notas de R$1')
    break
print('Volte sempre!')




