'''c = 1
while c == 1:
    sexo = str(input('Digite o sexo [M/F]: ')).strip()[0]
    if sexo in 'MmFf':
        print('Sexo valido!')
        c = 0
    else:
        print('Digite M ou F')
        c = 1'''

sexo = str(input('Digite o sexo [M/F]: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe seu sexo: ')).strip()[0]
print('Sexo {} registrado!'.format(sexo))

