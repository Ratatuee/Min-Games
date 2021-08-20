from random import randint
s1 = randint(1, 10)
s2 = randint(1, 3)
s3 = randint(1, 100)
coun = 0
n1 = 0
n4 = 0
a1 = str(input('Deseja ver as regras do jogo? ')).strip().upper()[0]
if a1 in 'S':
    print('Antes de tudo você escolhera o nivel de dificudade do jogo \nSera perguntado um número que você terá de avivinhar \nEsse número será pensado pelo própio computador')
else:
    print('Boa sorte')
while True:
    coun = 0
    print('\033[32m[1]Facil \n\033[33m[2]Médio \n\033[31m[3]Difícil\033[m')
    a2 = int(input('Selecione á dificuldade do jogo: '))
    print('                                            ')
    if a2 == 1:
        n1 = int(input('Adivinhe o número que estou pensando (1 á 3) : '))
        while n1 != s2:
            if n1 != s2:
                if s2 > n1:
                    n1 = int(input('Mais:'))
                    print('                                      ')
                else:
                    n1 = int(input('Menos: '))
                    print('                                       ')
                coun += 1
        if n1 == s2:
            if coun == 0:
                print('Você ganhou de primeira PARABENS!!')
            else:
                print('Você acertou com {} tentativas parabens'.format(coun))
    if a2 == 2:
        n2 = int(input('Adivinhe o número que estou pensando(1 á 10) '))
        while n2 != s1:
            if n2 != s1:
                if s1 > n2:
                    n2 = int(input('Mais:'))
                else:
                    n2 = int(input('Menos:'))
                coun += 1
        if n2 == s1:
            if coun == 0:
                print('Você ganhou de primeira PARABENS!!!')
            else:
                print('Você acertou com {} tentativas parabens'.format(coun))
    if a2 == 3:
        n3 = int(input('Adivinhe o número que estou pensando (1 á 100) '))
        while n3 != s3:
            if n3 != s3:
                if s3 > n3:
                    n3 = int(input('Mais:'))
                else:
                    n3 = int(input('Menos:'))
                coun += 1
            if n3 == s3:
                if coun == 0:
                    print('Você ganhou de primeira PARABENS!!!')
                else:
                    print('Você acertou com {} tentativas, parabens.'.format(coun))
    print('''[1]Jogar novamnte \n[0]Sair do jogo''')
    n4 = int(input('O que deseja- '))
    if n4 == 0:
        break
    print('                                      ')
from time import sleep
print('Finalizando...')
sleep(2)
print('Tchau! tchau!')
