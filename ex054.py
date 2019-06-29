from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('O numero de maiores de idade é: {}'.format(maior))
print('O numero de menores de idade é {}'.format(menor))