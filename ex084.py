galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = (str(input('Deseja continuar? S/N '))).strip().upper()[0]
    if continuar == 'N':
        break

# Ve o numero total de pessaos cadastradas
totalpessoas = len(galera)
print(f'Ao todo, você cadastrou {totalpessoas} pessoas')

# Ver o maior peso
print(f'O maior peso foi {maior}. Pertence as pessoas: ', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {menor}. Pertence as pessaoas: ', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')



# Meio modo. o de cima foi do professor guanabara o mais pika
'''# Maior peso
maior = galera[0][1]
for p, c in galera:
    if c > maior:
        maior = c
# Nome Maior
for nome, peso in galera:
    if peso == maior:
        nomemaior.append(nome)

print(f'O peso digiado foi {maior}. Peso de {nomemaior}')
print('*******')
# Menor peso
menor = galera[0][1]
for nome, peso in galera:
    if peso < menor:
        menor = peso
print(menor)'''


