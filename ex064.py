# Gambiarra que fiz
'''num = 0
digitados = 0
soma = 0
while num != 999:
    num = int(input('Digite o numero: '))
    digitados += 1
    soma += num

print('Foram {} numeros digitados, a soma entre eles é {}'.format(digitados - 1, soma - 999))'''

num = cont = soma = 0
num = int(input('Digite o numero: [999 para parar]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite o numero: [999 para parar]'))
print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))