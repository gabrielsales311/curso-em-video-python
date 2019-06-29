mil = total = menor = barato = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))

    # Total da compra
    total += preco

    # Precos com mais de 1000
    if preco > 1000:
        mil += 1

    # Nome do produto mais barato
    if menor == 0:
        menor = preco
        produtomenor = nome
    else:
        if preco < menor:
            menor = preco
            produtomenor = nome

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'O total da compra foi: R${total:10.2f}')
print(f'Produtos por mais de 1000 conto: {mil}')
print(f'Produto mais barato foi {produtomenor} que custa R${menor}')