frase = str(input('Digite a frase: ')).upper()
frasespace = frase.replace(' ', '')
frasenum = len(frasespace)

c2 = frasenum
condicao = 0

for c1 in range(0, frasenum):  # CONDIÇAO PRA VER DE FRENTE PRA TRAS
    n1 = frasespace[c1]
    c2 = c2 - 1
    n2 = frasespace[c2]
    if n1 != n2:
        condicao = 1
if condicao == 1:
    print('A frase "{}" não é um palindromo'.format(frase.capitalize()))
else:
    print('A frase  "{}" é um palindromo'.format(frase.capitalize()))
