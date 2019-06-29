# Tabuada usando FOR

n = int(input('Digite o numero: '))

for c in range(1, 11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
