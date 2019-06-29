from random import randint

# Coloca numeros aleatorios dentro da tupla
aleatorio = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

# Ver o menor numero da tupla
# print(min(aleatorio))
menor = sorted(aleatorio)[0]
# Ver o maior numero da tupla
# print(max(aleatorio))
maior = sorted(aleatorio)[-1]

print(aleatorio)
print(f'Menor: {menor}')
print(f'Maior: {maior}')

