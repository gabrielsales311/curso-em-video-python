n = float(input('Digite o salario do funcionario: '))

a = (n*15)/100
ns = n+a

print('O salario é {}, aumentou {} reais e o novo salario é {:.2f}'.format(n, a, ns))
