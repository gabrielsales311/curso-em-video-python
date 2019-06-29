valor = float(input('Digite o valor (R$): '))
print('''Em qual forma você deseja pagar?'
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opc = int(input('Digite a opção: '))

if opc == 1:
    total = valor - (valor * 10 / 100)
    print('O valor é R${}, ficou R${} com desconto'.format(valor, total))
elif opc == 2:
    total = valor - (valor * 5 / 100)
    print('O valor é R${}, ficou R${} com desconto'.format(valor, total))
elif opc == 3:
    total = valor
    parcela = valor / 2
    print('O valor da parela será R${}'.format(parcela))
elif opc == 4:
    total = valor + (valor * 20 / 100)
    numparcelas = int(input('Digite o numero de parcelas: '))
    parcela = total / numparcelas
    print('Sua compra sera parcelada em {} vezes de R${:.2f} com juros'.format(numparcelas, parcela))
    print('Valor final: {} '.format(total))
else:
    print('Opção invalida')