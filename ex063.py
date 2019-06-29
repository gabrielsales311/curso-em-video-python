termos = int(input('Digite quantos termos tu queres: '))
n1 = 0
n2 = 1
print('{} -> {}'.format(n1, n2),end=' ')
cont = 3
while cont <= termos:
    soma = n1 + n2
    print(' -> {}'.format(soma), end=' ')
    n1 = n2
    n2 = soma
    cont += 1
print(' -> FIM')
6