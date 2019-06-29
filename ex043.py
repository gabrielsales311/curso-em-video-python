peso = float(input('Seu peso em quilos: '))
altura = float(input('Sua altura em metros: '))
imc = peso / (altura ** 2)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc <30:
    print('Sobrepeso')
elif imc <40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
