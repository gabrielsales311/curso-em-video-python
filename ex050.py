# Ler 6 numeros inteiros; mostrar apenas os que forem pares
soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('Sâo {} numeros pares, a soma deles é: {}'.format(cont, soma))
