n1 = int(input('Digite o numero: '))
n2 = int(input('Digire o numero: '))
n3 = int(input('Digite o numero: '))

'''if n1 > n2 > n3 < n1:
    print('O maior numero é {}, o menor numero é {}'.format(n1, n3))
elif n1 > n2 < n3 < n1:
    print('O maior numero é {}, o menor numero é {}'.format(n1, n2))
elif n1 < n2 > n3 < n1:
    print('O maior numero é {}, o menor numero é {}'.format(n2, n3))
elif n1 < n2 > n3 > n1:
    print('O maior numero é {}, o menor numero é {}'.format(n2, n1))
elif n1 > n2 < n3 > n1:
    print('O maior numero é {}, o menor numero é {}'.format(n3, n2))
else:
    print('O maior numero é {}, o menor numero é {}'.format(n3, n1))'''

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))
