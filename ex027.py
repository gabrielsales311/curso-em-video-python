nome = str(input('Digite seu nome: ')).strip()
print('Prazer em te conhecer')
nomejunto = nome.split()  # separa cada palavra do nome
print('Seu primeiro nome é {}'.format(nomejunto[0]))
print('Seu ultimo nome é {}'.format(nomejunto[-1]))
