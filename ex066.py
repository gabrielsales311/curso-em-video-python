soma = digitados = 0
while True:
    num = int(input('Digite o numero [999 para parar]: '))
    if num == 999:
        break
    soma += num
    digitados += 1
print(f'Foram digitados {digitados} e a soma entre eles é {soma}')
