# Contagem regressiva; 10 segundos; com pausa de um segundo entre eles

from time import sleep
print('Contagem regressiva para o lançamento')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('LANÇADO')