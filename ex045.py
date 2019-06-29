from random import randint
from time import sleep

print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Digite a opção: '))
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

print('*' * 30)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('*' * 30)

if computador == 0:  # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:  # COMPUTADOR JOGOU PAPEL
        print('JOGADOR VENCEU')
    if jogador == 2:  # COMPUTADOR JOGOU TESOURA
        print('COMPUTADOR VENCEU')
#    else:
#        print('JOGADA INVALIDA')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCEU')
#    else:
#        print('JOGADA INVALIDA')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    if jogador == 2:
        print('EMPATE')
#    else:
#        print('JOGADA INVALIDA')
