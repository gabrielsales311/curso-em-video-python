print('Progressão Aritmética')
print('*=' * 10)

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 10
while c > 1:
    pt += r
    c -= 1
    print(pt, end=' ')
print('FIM')