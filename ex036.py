valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos = int(input('Em quantos anos vai pagar: '))

prestacao = valorcasa / (anos * 12)
porcentagemsalario = salario * 30/100

print ('Para pagar uma casa de R${} em {} anos a prestação sera de R${:.2f}'.format(valorcasa, anos, prestacao))

if prestacao > porcentagemsalario:
    excede = prestacao - porcentagemsalario
    print('Emprestimo negado. Prestação mensal excede R${:.2f} do limite de 30% do salario'.format(excede))
else:
    print('Emprestimo aceito!'.format(prestacao))
