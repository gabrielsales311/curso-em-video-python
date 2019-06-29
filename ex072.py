extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito','nove',
           'dez', 'onze', 'doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')
while True:
   num = int(input('Digite um numero entre 0 e 20: '))
   while num < 0 or num > 20:
      num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
   print(f'Você digitou o numero {extenso[num]}')
   continuar = ' '
   while continuar not in 'SN':
      continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
   if continuar == 'N':
      print('Flw irmão')
      break


