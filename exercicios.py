#num = int(input('Digite o numero'))
cores = {'branco' : '\033[30m' , 'vermelho':'\033[31m' , 'verde' : '\033[32m',
         'amarelo': '\033[33m' , 'azul': '\033[34m' , 'roxo' : '\033[35m',
         'azulclaro':'\033[36m' , 'cinza':'\033[37m' , 'limpa':'\033[m'
         } 
#print('O sucessor é {}{}{}'.format(cores['azulclaro'],num + 1,cores['limpa']) , end='//')
#print('O antecessor é {}{}{}'.format(cores['azul'],num - 1,cores['limpa']))

#num = int(input('Digite o numero: '))
#print('O dobro é {}{}{}'.format(cores['vermelho'],num*2,cores['limpa']) , end='//')
#print('O triplo é {}{}{}'.format(cores['azul'] , num*3 , cores['limpa']) , end='//')
#print('A raiz quadrada é {}{:.2f}{} '.format(cores['roxo'] , (num**(1/2)) , cores['limpa']))

#num1 = float(input('Digite a primeira nota'))
#num2 = float(input('Digite a segunda nota'))
#print('A média do aluno foi de: {}{}{}'.format(cores['azul'] , int(num1 + num2)/2 , cores['limpa']))

#num1 = int(input('Digite uma medida em metros: '))
#print('Aqui esta em centimetros: {}cm'.format(num1*100))
#print('Aqui esta em milimetros: {}mm'.format(num1*1000))

#num1 = int(input('Digite um numero: '))
#print('{} X 1: {}'.format(num1 , num1*1))
#print('{} X 2: {}'.format(num1 , num1*2))
#print('{} X 3: {}'.format(num1 , num1*3))
#print('{} X 4: {}'.format(num1 , num1*4))
#print('{} X 5: {}'.format(num1 , num1*5))
#print('{} X 6: {}'.format(num1 , num1*6))
#print('{} X 7: {}'.format(num1 , num1*7))
#print('{} X 8: {}'.format(num1 , num1*8))
#print('{} X 9: {}'.format(num1 , num1*9))
#n = float(input('Digite a quantidade em reais: '))
#print('A quantidade em dólares que vc possui é de: {}'.format(n/3.27))

#b = int(input('Digite a base da parede: '))
#h = int(input('Digite a altura da parede: '))
#print('A área da parede é de: {}m2'.format(b*h))
#print('A quantidade de tinta para pintar necessária é de: {}L'.format(b*h/2))

#p = float(input('Preço do produto: '))
#print('preço do produto descontado de 5%: {}'.format(p*95/100))

#s = float(input('Valor do salario: '))
#print('Salario com 15% de aumento: {}'.format(s*115/100))

#DESAFIOS AULA 8

#import math
#n = float(input('Digite qualquer numero com casas decimais: '))
#print('A parte inteira é de: {}'.format(int(n)))

#n1 = float(input('Digite o cateto oposto: '))
#n2 = float(input('Digite o cateto adjacente: '))
#res1 = n1**2 + n2**2
#print('Resultado é: {}'.format(math.sqrt(res1)))

#ang = float(input('Digite um angulo em graus: '))
#print('O seno dele é: {}'.format(math.sin(math.radians(ang))))

#from random import shuffle

#lista = ['Rafael' , 'Cicrano' , 'Otavio' , 'Fulano']
#shuffle(lista)
#print(lista)

#n = input('Digite o nome completo: ')

#print(n.upper())
#print(n.lower())

#dividido = n.split()
#n1 = len(dividido[0])
#n2 = len(dividido[1])
#n3 = len(dividido[2])

#NUMERO DE LETRAS DO NOME COMPLETO
#print('letras ao todo: {}'.format(n1 + n2 + n3))
#print('numero de letras do primeiro nome: {}'.format(n1))

#UNIDADE ATE MILHAR DE NUMERO
#n = int(input('Digite um numero de 0 a 9999: '))
#dividido = ' '.join(n).split()

#n1 = n % 10
#n = int(n / 10)
#n2 = n % 10
#n = int(n / 10)
#n3 = n % 10
#n = int(n / 10)
#n4 = n % 10
#n = int(n / 10)
#if(n1 != 0):
#    print('unidade: {}'.format(n1))
#if(n2 != 0):
#     print('dezena: {}'.format(n2))
#if(n3 != 0):
#     print('centena: {}'.format(n3))
#if(n4 != 0):    
#    print('milhar: {}'.format(n4))

#COMEÇA OU NÃO COM SANTO A CIDADE?
#nome = input('Digite o nome de uma cidade: ')
#dividido = nome.split()
#if(dividido[0] == 'SANTO'):
#    print('começa sim')
#else:
#    print('começa não')

#frase = input('Digite a frase: ')
#frase.strip()
#print('numero de As: {}'.format(frase.count('A')))
#print('primeiro A: {}'.format(frase.find('A')))
#print('ultimo A: {}'.format(frase.find('A' , frase.find('A') + 1)))



