'''from random import randint
from time import sleep
cont = 1
tot = 1
print('Pensando em um numero...')
sleep(1)
computador = randint(0, 10)
print('Pensei! Agora tente adivinhar!')
while cont == 1:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    if jogador == computador:
        print('Você advinhou!\nNumero de tentativas: {}'.format(tot))
        cont = 0
    else:
        print('Tente novamente')
        tot += 1'''
from random import randint
computador = randint(0, 10)
print('Advinhe o numero que pensei, humano.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Seu palpite entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Foi mais')
        else:
            print('Foi menos')

print('Você acertou! Numero de tentativas: {}'.format(palpites))
