'''from random import choice

num = int(input('Digite um numero de 0 a 5: '))

lista = [1, 2, 3, 4, 5]
escolhido = choice(lista)

if num == escolhido:
    print('Você advinhou o numero escolhido! {}'.format(escolhido))
else:
    print('Vocé digitou {} e o computador escolheu {}'.format(num, escolhido))'''  #  Minha solução


#  solução do professor


from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Pensando em um numero entre 0 e 5')
print('-=-' * 20)

jogador = int(input('Em que numero pensei? '))
print('Processando...')
sleep(1) #  computador para para simular uma pensada
if jogador == computador:
    print('Parabénss! Você acertou')
else:
    print('Errou! Escolhi {} e você digitou {}'.format(computador, jogador))
