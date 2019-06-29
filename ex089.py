boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, nota1, nota2, media])
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

c = 0
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
while c <= len(boletim) - 1:
    print(f'{c:<4}{boletim[c][0]:<10}{boletim[c][3]:>8.1f}')
    c += 1

while True:
    notas = int(input('Deseja mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    if notas <= len(boletim) - 1:
        print(f'Notas de {boletim[notas][0]} são {boletim[notas][1:3]}')
