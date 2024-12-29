#import pygame
#pygame.init()
#print('Contagem regressiva fogos de artifício! ')
#c = 0
#for c in range (10 , 0  , -1):
#    pygame.time.delay(1000)
#    print('{}{}{}'.format('\033[31m' , c , '\033[m'))
#    pygame.quit()
#print('Happy new year!')

#s = 0
#for c in range(1 , 500 , 2):
#    if(c % 3 == 0):
#        s +=c
#print(s)

#TABUADA
#n = int(input('Digite um valor do qual vc quer ver a tabuada: '))
#for c in range(1 , 10):
#    print('{} X {} = {}'.format(n , c , c*n))

#SOMA PARES
#s = 0
#for c in range (0 , 6):
#    n = int(input('Digite o valor: '))
#    if(n % 2 == 0):
#        s = s + n
#print('Essa é a soma dos pares: {}'.format(s))

#P.A
#n1 = int(input('Digite o primeiro termo da P.A: '))
#r = int(input('Digite a razão da P.A: '))
#print('Os 10 termos são: ')
#for c in range(n1 , n1 + 9*r + 1, r):
#    print(c)

#NUMEROS PRIMOS

#n = int(input('Digite para verificar se é número primo ou não: '))
#count = 0
#for c in range (1 , n + 1):
#    if(n % c == 0):
#        count = count + 1
#if(count == 2):
#    print('É primo')
#else:
#    print('Não é primo')

#Verificação de palavras palindromas

#p1 = str(input('Digite a palavra: ')).strip().upper()
#separado1 = p1.split()
#p11 = ''.join(separado1)
#inverso = ''
#for i in range (len(p11) -1 , -1 , -1):
#    inverso = inverso + p11[i]
#if(inverso == p11):
#    print('é palíndromo')    
#else:
#    print('Não é palíndromo')

#DATA DE NASCIMENTO DE 7 PESSOAS
#countMaior = 0
#for c in range (1 , 8):
#    n = int(input('Digite o ano de nascimento: '))
#    if(2024 - n >= 21):
#        countMaior = countMaior + 1
#print('Numero de pessoas que é de maior: {}'.format(countMaior))        


#p = int(input('Digite o peso da pessoa: '))
#min = p
#max = p
#for i in range (0 , 4):
#    p = int(input('Digite o peso da pessoa: '))
#    if(p > max):
#        max = p
#    if(p < min):
#        min = p
#print('Peso maximo: {}Kg , Peso minimo: {}Kg'.format(max , min))

#NOME IDADE E SEXO

#soma = 0
#max = 0
#countMulher = 0
#nome = str(input('Digite o nome: '))
#i = int(input('Digite a idade: '))
#sexo = str(input('Digite o sexo: '))
#nomeMaisVelho = nome
#idadeMaisVelho = i
#if(sexo == "mulher" and i < 20):
#    countMulher = countMulher + 1
#soma = soma + i
#if(sexo == "homem"):
#    nomeMaisVelho = nome
#    max = i
#for i in range(0 , 3):
#    nome = str(input('Digite o nome: '))
#    i = int(input('Digite a idade: '))
#    sexo = str(input('Digite o sexo: '))
#    nomeMaisVelho = nome
#    idadeMaisVelho = i
#    if(i > max and sexo == "homem"):
#        max = i
#       nomeMaisVelho = nome
#    if(sexo == "mulher" and i < 20):
#        countMulher = countMulher + 1
#    soma = soma + i
#print('Media deu: {}'.format(soma/4))
#print('Nome do homem mais velho é: {}'.format(nomeMaisVelho))
#print('Numero de mulheres com menos de 20: {}'.format(countMulher))


