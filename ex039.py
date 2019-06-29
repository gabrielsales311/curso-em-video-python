from datetime import date
nasc = int(input('Digite o ano do nascimento: '))
atual = date.today().year
idade = atual - nasc

print('Você tem {} anos.'.format(idade))

if idade < 18:
    saldo = (18 - idade)
    print('Ainda não é hora de se alistar, faltam {} ano(s)'.format(saldo))
    ano = atual + saldo
    print('Você vai se alistar em {}'.format(ano))
elif idade > 18:
    saldo = (idade - 18)
    print('Já passou o tempo de se alistar, passaram-se {} ano(s) do prazo.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Hora de se alistar!')
