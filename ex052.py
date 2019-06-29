n = int(input('Digite o numero: '))
total = 0
for c in range(2, n):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(' {} '.format(c), end='')


if total > 1:
    print('\n O numero {} não é primo, ele é divisivel por {} numeros'.format(n, total))
else:
    print('\n O numero {} é primo'.format(n))
