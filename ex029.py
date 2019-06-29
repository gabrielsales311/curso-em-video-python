num = float(input('Digite a velocidade do carro: '))

if num >= 80:
    multa = (num - 80) * 7
    print('Você esta {} acima da velocidade maxima de 200km, sua multa é {}'.format(num - 80, multa))
else:
    print("Você esta dentro do limite de velocidade.")
