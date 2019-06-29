salario = float(input('Digite o valor do salario: '))

if salario > 1250:
    print('O salario com aumento fica: {}'.format(salario + (salario * 10 / 100)))
else:
    print('O salario com aumento fica: {}'.format(salario + (salario * 15 / 100)))

