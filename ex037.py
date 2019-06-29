num = int(input('Digite o numero: '))

binario = bin(num)[2:]
hexa = hex(num)[2:]
octal = oct(num)[2:]
print ('-=-' * 20)
opc = int(input(''''Digite a opção desejada:
1 - Conveter pra binario 
2 - Converter para hexadecimal 
3 - Converter para octal: '''''))

if opc == 1:
    print('O numero {} em binario é {}'.format(num, binario))
elif opc == 2:
    print('O numero {} em hexadecimal é {}'.format(num, hexa))
elif opc == 3:
    print('O numero {} em octal é {}'.format(num, octal))
else:
    print('Opcao invalida. Tente novamente')
