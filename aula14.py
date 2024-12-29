#c = 1
#while c < 10:
#    print(c)
#    c = c + 1
#print('Fim')

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N]')).upper()
#print('Fim')

#countPar = countImpar = 0
#n = int(input('Digite um valor: '))
#while(n != 0):
#    if(n%2 == 0):
#        countPar += 1
#    else:
#        countImpar += 1
#    n = int(input('Digite um valor: '))
#print('Countpar: {} e CountImpar: {}'.format(countPar , countImpar) )

#DESAFIO

#r = str(input('Digite seu sexo [M/F]: ')).upper()
#while(r != 'M' and r != 'F'):
#    print('Digite M ou F')
#    r = str(input('Digite seu sexo [M/F]')).upper()


#import random
#n = int(input('Digite um numero de 0 a 10: '))
#c = random.randint(0 , 10)
#while(n != c):
#    n = int(input('Digite um numero de 0 a 10: '))
#print('Você acertou!')

#n1 = int(input('Digite o primeiro numero: '))
#n2 = int(input('Digite o segundo numero: '))
#print('''
#    [1]somar
#    [2]multiplicar
#    [3]maior
#    [4]novos números
#    [5]sair do programa
#''')
#n = int(input(('Digite a opção desejada: ')))
#while(n != 5):
#    if(n == 1):
#        print('Soma deu: {}'.format(n1 + n2))
#    elif(n == 2):
##        print('A multiplicação deu: {}'.format(n1*n2))
#    elif(n == 3):
#        if(n1 > n2):
#            print('O maior entre eles foi o: {}'.format(n1))
#        else:
#            print('O maior entre eles foi o: {}'.format(n2))
#    elif(n == 4):
##        n1 = int(input('Digite o primeiro numero: '))
#        n2 = int(input('Digite o segundo numero: '))
#    print('''
#    [1]somar
#    [2]multiplicar
#    [3]maior
#    [4]novos números
#    [5]sair do programa
#    ''')
#    n = int(input(('Digite a opção desejada: ')))
#print('Fim do programa!')

#FATORIAL1

#n = int(input('Digite o numero para calcular seu fatorial: '))
##res = 1
#for c in range (n , 0 , -1):
#    res = res*c
#print('O resultado do fatorial deu: {}'.format(res))

#FATORIAL2
#n = int(input('Digite o numero para calcular seu fatorial: '))
#i = n
#res = 1
#while(i > 1):
#    res = res*i
#    i = i - 1
#print('O fatorial deu: {}'.format(res))

#P.A
#p1 = int(input('primeiro termo da P.A: '))
#r = int(input('Razao da P.A: '))
#i = p1
#while(i <= p1 + 9*r):
#    print('Termo da P.A: {}'.format(i))
#    i = i + r
#print('Fim')

#continuação P.A
#p1 = int(input('primeiro termo da P.A: '))
#r = int(input('Razao da P.A: '))
#i = p1
#while(i <= p1 + 9*r):
#    print('Termo da P.A: {}'.format(i))
#    i = i + r
#print('Fim')
#n = int(input('quantos termos mais você quer ver? '))
#while(n != 0):
#    p2 = i
#    while(i < p2 + n*r):
#        print('Termo da P.A: {}'.format(i))
#        i = i + r
#    n = int(input('quantos termos mais você quer ver? '))
#print('FIM')

#SEQUENCIA DE FIBONACCI

#n = int(input('Digite o numero de elementos que vc quer ver da sequencia: '))
#n1 = 0
#n2 = 1
#i = 2
#if(n == 1):
#    print(n1)
#if(n >= 2):
#    print(n1)
#    print(n2)
#    while(i < n):
#        n3 = n1 + n2
#        print(n3)
#        n1 = n2
#        n2 = n3
#        i += 1

#SEQUENCIA DE NUMEROS INTEIROS

#s = ''
#n = int(input('Digite o numero: '))
#soma = n
#count = 1
#max = n
#min = n
#s = str(input('Quer continuar [S/N]? ')).upper()
#while(s != 'N'):
#    n = int(input('Digite o numero: '))
#    soma += n
#    count += 1
#    if(n > max):
#        max = n
#    if(n < min):
#        min = n
#    s = str(input('Quer continuar [S/N]? ')).upper()
#print('Média deu: {}'.format(soma/count))
#print('O maior valor deu: {}'.format(max))
#print('O menor valor deu: {}'.format(min))

