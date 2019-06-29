num = []
maior = menor = 0
for cont in range(0, 5):
    num.append(int(input(f'Digite valor para posição {cont}: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]

print('*=' *30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições: ', end=' ')
for posicao, valores in enumerate(num):
    if valores == maior:
        print(posicao, end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end=' ')
for posicao, valores in enumerate(num):
    if valores == menor:
        print(posicao, end=' ')
