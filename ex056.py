somaidade = 0
maior = 0
vinte = 0

for c in range(1, 5):
    print('-----{}ª pessoa-----'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('[M] Masculino [F] Feminino: '))

    # Calcular a media de idade
    somaidade += idade
    media = somaidade / 4

    # Nome do homem mais velho
    if sexo in 'Mm' and idade > maior:
        maisvelho = nome
        maior = idade

    if sexo in 'Ff' and idade < 20:
        vinte += 1

print('A media de idade do grupo é: {}'.format(media))
print('O homem mais velho é o {}'.format(maisvelho))
print('Quantas mulheres tem menos de 20 anos: {}'.format(vinte))