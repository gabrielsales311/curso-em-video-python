n1 = float(input('Digite a largura da parede: '))
n2 = float(input('Digite a altura da parede: '))

area = n1*n2
litro = area/2

print('A área da parede é {}m² \n Será ecessario {:.2f} litros de tinta.'.format(area, litro))
