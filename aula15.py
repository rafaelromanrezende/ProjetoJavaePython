#uso de f string

#nome = 'José'
#idade = 33
#print(f'O {nome} tem {idade} anos')

#n = int(input('Digite o numero [999 para]: '))
#count = 1
#soma = n
#while(True):
#    n = int(input('Digite o numero [999 para]: '))
#    if(n == 999):
#        break
#    soma += n
#    count += 1
#print(f'A soma dos {count} valores deu: {soma}')

#TABUADA
#n = int(input('Digite o numero para ver sua tabuada: '))
#while(n > 0):
#    print('{} X 1 = {}'.format(n , n*1))
#    print('{} X 2 = {}'.format(n , n*2))
#    print('{} X 3 = {}'.format(n , n*3))
#    print('{} X 4 = {}'.format(n , n*4))
##    print('{} X 5 = {}'.format(n , n*5))
#    print('{} X 6 = {}'.format(n , n*6))
#    print('{} X 7 = {}'.format(n , n*7))
#    print('{} X 8 = {}'.format(n , n*8))
#    print('{} X 9 = {}'.format(n , n*9))
#    n = int(input('Digite o numero para ver sua tabuada: '))

#PAR OU IMPAR
#import random

#c  = random.randint(0 , 10)
#v = 0
#e = str(input('Digite par ou impar: '))
#n = int(input('Digite o numero escolhido: '))
#while True:
#    if e == 'par':
##        if ((n + c) % 2 == 0):
#            print('Computador escolheu {}'.format(c))
#            print('Você ganhou dessa vez')
#            v += 1
#        else:
#            print('Perdeu')
#            print('Computador escolheu {}'.format(c))
#            break
#    elif e == 'impar':
#        if ((n + c) % 2 != 0):
#             print('Computador escolheu {}'.format(c))
#             print('Você ganhou dessa vez')
#             v += 1
#        else:
#            print('Perdeu')
#            print('Computador escolheu {}'.format(c))
#            break
#    c  = random.randint(0 , 10)
#    e = str(input('Digite par ou impar: '))
#    n = int(input('Digite o numero escolhido: '))
#print('O número de vitórias consecutivas foi de: {}'.format(v))

#CADASTRO DE PESSOAS

#s = ''
#countMais18 = countH = countM20 = 0
#while(s != 'N'):
#    i = int(input('Digite a sua idade:'))
#    sexo = str(input('Digite o seu sexo: [H/M]')).upper()
#    if(i >= 18):
#        countMais18 += 1
#    if(i < 20 and sexo == 'M'):
#        countM20 += 1
#    if(sexo == 'H'):
#        countH += 1
#    s = str(input('Você quer continuar? [S/N]')).upper()

#print(f'Numero de homens : {countH}')
#print(f'Numero de mulheres com menos de 20 anos: {countM20}')
#print(f'Numero de pessoas com mais de 18 anos: {countMais18}')

#CAIXA ELERONICO
#print('----------------------')
#print('Bem vindo ao caixa!')
#print('----------------------')
#n = int(input('Qual o valor a ser sacado?'))
#c50 = int(n / 50)
#c20 = int((n % 50) / 20)
#c10 = int(((n % 50) % 20) / 10)
#c1 = int((((n % 50) % 20) % 10) / 1)
#print(f'As cedulas de 50 serão: {c50}, de 20: {c20} , de 10: {c10} , de 1: {c1}')