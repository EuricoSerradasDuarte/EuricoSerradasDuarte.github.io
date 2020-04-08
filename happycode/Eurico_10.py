#!/usr/bin/python
# vim: set fileencoding=\xc3 :

import random
bull = 0
cow = 0
print("Bem-vindo ao Bulls and Cows. Para jogar, escreva uma palavra com 5 letras e cujas letras não se repitam.\nTerá de adivinhar qual é a palavra secreta. Para isso deve seguir as dicas dadas baseadas na palavra que inseriu:\n    -um bull indica que uma letra corresponde a outra na mesma posição na palavra secreta;\n    -um cow indica que uma letra existe na palavra secreta, mas está na posição errada.\nBoa sorte!")
secreta = random.choice( ["besta", "mitos", "celas", "mosca", "amigo", "ondas", "velha"] )

while bull!=5:
    insert = str(input("\nInsira a sua palavra: "))
    if len(insert)==5: 
        if secreta==insert:
            print("Parabéns, está correto!")
            repeat = str(input("Gostaria de jogar novamente? (s, n): "))
            if repeat=="s":
                secreta = random.choice( ["besta", "mitos", "celas", "mosca", "amigo", "ondas", "velha"] )
                bull=0
            if repeat=="n":
                bull=5
        else:
            if insert[0]==secreta[0]:
                bull = bull + 1
            if insert[0]==secreta[1] or insert[0]==secreta[2] or insert[0]==secreta[3] or insert[0]==secreta[4]:
                cow = cow + 1

            if insert[1]==secreta[1]:
                bull = bull + 1
            if insert[1]==secreta[0] or insert[1]==secreta[2] or insert[1]==secreta[3] or insert[1]==secreta[4]:
                cow = cow + 1

            if insert[2]==secreta[2]:
                bull = bull + 1
            if insert[2]==secreta[0] or insert[2]==secreta[1] or insert[2]==secreta[3] or insert[2]==secreta[4]:
                cow = cow + 1

            if insert[3]==secreta[3]:
                bull = bull + 1
            if insert[3]==secreta[0] or insert[3]==secreta[1] or insert[3]==secreta[2] or insert[3]==secreta[4]:
                cow = cow + 1

            if insert[4]==secreta[4]:
                bull = bull + 1
            if insert[4]==secreta[0] or insert[4]==secreta[1] or insert[4]==secreta[2] or insert[4]==secreta[3]:
                cow = cow + 1

            print(str(bull), "bull(s),\n"+str(cow), "cow(s).")
            bull = 0
            cow = 0
    else:
        print("Insira um palavra com 5 letras!")
