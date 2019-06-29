a = float(input("Digite lado 1: "))
b = float(input("Digite lado 2: "))
c = float(input("Digite lado 3: "))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Pode formar triangulo')
else:
    print('Não pode formar triangulo')
