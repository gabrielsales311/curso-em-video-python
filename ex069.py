adulto = homens = mulhervinte = 0
while True:
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Invalido. Digite o sexo [M/F]: '))
    print('-' * 30)

    # Mais de 18 anos
    if idade > 18:
        adulto += 1
    # Quantos homens foram cadastrados
    if sexo in 'Mm':
        homens += 1
    # Mulher com menos de vinte anos
    if sexo in 'Ff'and idade < 20:
        mulhervinte += 1

    continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continuar in 'Nn':
        break
print(f'Temos {adulto} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'E temos {mulhervinte} mulheres com menos de 20 anos')
