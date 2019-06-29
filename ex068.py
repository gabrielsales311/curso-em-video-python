from random import randint
total = 1
while True:
    numjogador = int(input('Diga o valor: '))
    escolhajogador = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    while escolhajogador not in 'PpIi':
        escolhajogador = str(input('Invalido. Par ou impar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    resultado = numjogador + computador
    if resultado % 2 == 0:
        jogo = 'P'
        print(f'Voce jogou {numjogador}, o computador jogou {computador}, o resultado foi {resultado} DEU PAR')
    else:
        jogo = 'I'
        print(f'Voce jogou {numjogador}, o computador jogou {computador}, o resultado foi {resultado} DEU IMPAR')
    if jogo == escolhajogador:
        print('Você venceu!')
        print('Jogar novamente...')
        total += 1
    else:
        print('-' * 30)
        print('Perdeu irmão')
        print(f'Total de jogadas {total}')
        print(' ' * 20)
        break
