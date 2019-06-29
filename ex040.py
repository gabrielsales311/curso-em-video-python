nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado. Média: {}'.format(media))
elif 7 > media >=5:
    print('Recuperação. Média: {}'.format(media))
elif media >= 7:
    print('\033[1;33mAprovado!.\033[m Média: {}'.format(media))
