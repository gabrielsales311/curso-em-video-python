# GAMBIARRA QUE FIZ
'''palavras = ('curso', 'programar', 'haha', 'python')
numpalavras = len(palavras)
teste = 'haha'
numteste = len(teste)

for cont in range(0, numpalavras):
    palavra = palavras[cont]
    print(palavra)
    for cont2 in range(0, len(palavra)):
        letra = palavra[cont2]
        print(letra)
        if letra == 'a':
            a = 'a'
            print(a, end='')
        elif letra == 'e':
            e = 'e'
        elif letra == 'i':
            i = 'i'
        elif letra == 'o':
            o = 'o'
        elif letra == 'u':
            u = 'u'

# print(len(palavras[2]))'''

palavras = ('curso', 'programar', 'haha', 'python')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
