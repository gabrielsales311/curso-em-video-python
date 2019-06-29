n = float(input('Digite o preço do produto: '))

desc = (5*n)/100
novopreco = n-desc

print('O preço é {}, com desconto de 5% fica {:.2f}'.format(n, novopreco))
