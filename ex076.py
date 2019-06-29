lista = ('Pao', 1,
         'Leite', 3.50,
         'Borracha', 30,
         'Caderno', 400,
         'Camisa do Verdão', 340)
prod = lista[0::2]
preco = lista[1::2]
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for c in range(0, len(preco)):
    print(f'{prod[c]:.<30}R${preco[c]:>7.2f}')
