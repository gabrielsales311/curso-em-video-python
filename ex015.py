km = float(input('Quantidade de KM rodados: '))
dia = float(input('Quantidade de dias: '))

#custodia = dia * 60
#custokm = km * 0.15

custo = (dia*60)+(km * 0.15)

print('O total a pagar é: R${:.2f}'.format(custo))
