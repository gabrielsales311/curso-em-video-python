frase = str(input('Digite a frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A esta na posição {}'.format(frase.find('A')+1))
print('A ultima letra A esta na posição {}'.format(frase.rfind('A')+1))  # O RFIND procura a palavra da direita pra esquerda
