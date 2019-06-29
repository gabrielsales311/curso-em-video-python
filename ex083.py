expressao = str(input('Digite a expressão: '))
pa = 0
pf = 0

for valor in expressao:
    if valor == '(':
        pa += 1
    if valor == ')':
        pf += 1
if pa == pf:
    print('Valido')
else:
    print('invalido')