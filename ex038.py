num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

if num1 > num2:
    print('O numero {} é maior'.format(num1))
elif num2 > num1:
    print('O numero {} é maior'.format(num2))
else:
    print('Os numeros são iguais')