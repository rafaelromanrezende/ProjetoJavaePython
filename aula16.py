#Variavel composta
#TUPLA
#lanche = ('Hamburguer' , 'suco' , 'pizza' , 'pudim')
#print(lanche[-2])
#for c in lanche:
#    print(f'Vou comer {c}')
#print('comi demais!')

#for i in range (0 , len(lanche)):
#    print(f'Vou comer {lanche[i]}')
#print('Comi demais!')

#for pos , comida in enumerate (lanche):
#    print(f'Eu vou comer a comida {comida} , na posição {pos}')
#print('Comi demais!')

#a = (1 , 2 , 3 , 4)
#b = (5 , 6 , 6 , 8)
#c = a + b
#print(c.index(6))

#DESAFIO NUMERO POR EXTENSO

#contagem = ('zero' , 'um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' ,'dezesseis' ,'dezessete' , 'dezoito' , 'dezenove' , 'vinte')
#for c in contagem:
#    n = int(input('Digite um numero que gostaria de ver por extenso: '))
#    if(n > 0):
#       print(contagem[n])
#    else:
#       print('Tente novamente')

#BRASILEIRAO
#times = ('botafogo' , 'palemiras' , 'flamengo' , 'fortaleza' , 'inter' , 'sp' , 'corinthians' , 'bahia' , 'cruzeiro' , 'vasco da gama')
#print('Melhores 5 times: ')
#for c in range (0 , 5):
#    print(f' Time {times[c]} esta na posição {c + 1}')
#print('Piores 4 times: ')
#for i in range (6 , 10):
#    print(f' Time {times[i]} esta na posição {i + 1}')
#print(f'Times em ordem alfabética: {sorted(times)}')
#print('Posição na qual ficou o time do palmeiras: ')
#print(times.index('palemiras') + 1)

#TUPLA ALEATORIA
#import random
#n1 = random.randint(0 , 10)
#n2 = random.randint(0 , 10)
#n3 = random.randint(0 , 10)
#n4 = random.randint(0 , 10)
#n5 = random.randint(0 , 10)
#max = n1
#min = n1
#tupla = (n1 , n2 , n3 , n4 , n5)
#print(f'Tupla gerada: {tupla}')
#for c in range (1 , 5):
#    if(tupla[c] > max):
##        max = tupla[c]
#    if(tupla[c] < min):
#        min = tupla[c]
#print(f'O maior da tupla é: {max}')
#print(f'O menor da tupla é: {min}')

#TUPLA LIDA DO TECLADO

tupla = ()
tuplaP = ()
for c in range (0 , 4):
    n = int(input('Digite um valor para colocar na tupla: '))
    tupla += n
    if(n % 2 == 0):
        tuplaP += n
print('Numero de vezes que apareceu o 9: ')
print(tupla.count(9))
print('Posição que apareceu o primeiro valor 3: ')
print(tupla.index(3))
print('Numeros pares que apareceram: ')
print(tuplaP)

