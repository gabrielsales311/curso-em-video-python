num = float(input('Digite a distancia da viagem: '))

if num <= 200:
    passagem = num * 0.50
    print('O preço da viagem é: {}'.format(passagem))
else:
    passagem = num * 0.45
    print('O preço da viagem é: {}'.format(passagem))
