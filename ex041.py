from datetime import date
anonasc = int(input('Digite o ano de nascimento: '))

idade = date.today().year - anonasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
