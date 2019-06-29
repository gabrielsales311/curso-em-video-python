lista = []
for c in range(0, 5):
    num = (int(input('Digite um numero: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado na ultima posição da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')