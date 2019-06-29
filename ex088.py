from random import randint
from time import sleep
numjogos = int(input('Quantos jogos você quer: '))
print(f'Sortetando {numjogos} jogos')
jogo = []
apostas = []
for j in range(0, numjogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    apostas.append(jogo[:])
    print(f'Jogo {j + 1}: {apostas[j]}')
    jogo.clear()
    sleep(0.5)
