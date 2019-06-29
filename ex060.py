numero = int(input('Digite um número: '))
cont = numero
fatorial = 1
print('Fatorial de {}! = '.format(numero), end=' ')
while cont > 0:
    print('{}'.format(cont), end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))

'''from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''