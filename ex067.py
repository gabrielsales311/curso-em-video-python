'''num = int(input('Digite o numero: '))
multi = 1
while True:
    if num < 0:
        break
    resultado = num * multi
    print(f'{num} x {multi} = {resultado}')
    multi += 1
    if multi == 11:
        num = (int(input('Digite o numero: ')))
        multi = 1
        if num < 0:
            print('Volte sempre')
            break'''
while True:
    num = (int(input('Digite o numero: ')))
    if num < 0:
        print('Volte sempre.')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')