# Razão aritmetica; Ler primeiro termo e a razão; Mostrar os 10 primeiros termos da progressão
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print(pt, end=' ')
for c in range(0, 9):
    pt = pt + r
    print(pt, end=' ')
print('Acabou')
