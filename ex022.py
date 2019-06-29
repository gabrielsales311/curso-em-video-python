nome = str(input("Digite seu nome: "))

'''mai = nome.upper()  # deixa a frase em maiusculo
min = nome.lower()  # deixa a frase em minusculo
letras = nome.replace(' ', '')  # substitui os espaços por algo, nesse caso por nada pra deixar as letras juntas
num = len(letras)  # conta o numero de letras e espaços, nesse caso a frase não tem espaços
listarnome = nome.split()  # separa cada nome em um lista
pnome = listarnome[0]  # pega o primeiro nome
pnomenum = len(pnome)

print("Seu nome em maiusculas é {} "
      "\nSeu nome em minusculas é {} "
      "\nSeu nome tem {} letras "
      "\nSeu primeiro nome é {} e ele tem {} letras".format(mai, min, num, pnome, pnomenum))'''

# Fazendo o mesmo exercicio anterior só que sem com menos variaveis

print("Seu nome em maiusculas é: {}".format(nome.upper()))
print("Seu nome em minusculas é: {}".format(nome.lower()))
semespaco = nome.replace(' ', '')
print("Seu nome tem {} letras".format(len(semespaco)))
listarnome = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(listarnome[0], len(listarnome[0])))


