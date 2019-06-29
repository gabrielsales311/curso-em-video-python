num = [[], []]
for c in range(0, 7):
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')
