tup = (int(input('Digite o numero: ')),
       int(input('Digite o outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')),
       )
print('*' * 30)
print(tup)
print('*' * 30)

# Quantas vezes apareceu o 9
print(f'O numero nove apareceu {tup.count(9)} vezes')

if 3 in tup:
    posicao3 = tup.index(3) + 1
    print(f'O numero 3 apareceu pela primeira vez na posição: {posicao3}')
else:
    print('Não tem 3 não amigo.')

# Quais foram os numeros pares
print('Os numeros pares são: ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')