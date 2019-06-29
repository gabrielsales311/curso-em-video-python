brasileirao = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético-MG', 'Goiás',
               'Botafogo', 'Bahia', 'São Paulo', 'Corinthians', 'Grêmio', 'Athletico-PR', 'Ceará',
               'Fortaleza','Vasco','Fluminense','Chapecoense','Cruzeiro','CSA','Avaí')

primeiros = brasileirao[0:5]
print('Os primeiros times são')
print(primeiros)
print('-=' * 30)

ultimos = brasileirao[-4:]
print('Os ultimos são:')
print(ultimos)
print('-=' * 30)

# Sorted deixa em ordem alfabetica
print('Em ordem alfabetica é:')
ordem = sorted(brasileirao)
print(ordem)
print('-=' * 30)

# Achar a posição
chape = brasileirao.index('Chapecoense')
print(f'A chapecoense esta na {chape + 1}ª posição')
