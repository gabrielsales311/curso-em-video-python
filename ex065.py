maior = menor = 0
soma = 0
digitados = 0
sair = 'Ss'
while sair in 'Ss':
    num = int(input('Digite o numero: '))
    soma += num
    digitados += 1
    if menor == 0 and maior == 0:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sair = str(input('Deseja continuar?[S/N] '))

media = soma / digitados
print('Foram digitados {} numeros. A media entre eles é {}'.format(digitados, media))
print('O maior numero digitado foi {}, o menor foi {}'.format(maior, menor))
