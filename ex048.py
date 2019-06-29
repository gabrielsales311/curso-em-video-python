# Soma dos numeros impares, multiplos de tres entre 1 ate 500
soma = 0
cont = 0
print('Os numeros impares e multiplos de tres são: ')
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c

print('A soma desses {} numeros é: {} '.format(cont, soma))

