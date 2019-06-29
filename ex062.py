pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 10
programa = 1

while programa != 0:
    while c > 0:
        pt += r
        termos = pt
        c -= 1
        print(termos, end=' ')
    if programa != 0:
        c = int(input('\nMais: '))
        programa = c

print('Falou irmão!')