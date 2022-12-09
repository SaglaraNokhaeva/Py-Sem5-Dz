# Создайте программу для игры в ""Крестики-нолики"
input("Игра 'Крестики-нолики'. Два игрока поочерёдно делают ход." )
input("" )
str1=['H','H','H']
str2=['H','H','H']
str3=['H','H','H']
print(''.join(str1))
print(''.join(str2))
print(''.join(str3))
count=0
flag=0
steps=[]
while (flag==0):
    if (count>=9):
        input("Ничья!")
        break
    else:
        input("Ход 1-го игрока")
        x1=int(input("Задайте позицию строки крестика (1-3): "))
        y1=int(input("Задайте позицию столбца крестика(1-3): "))
        count+=1
        print(count)
        if x1==1:
            str1[y1-1]="X"
        elif x1==2:
            str2[y1-1]="X"
        else:
            str3[y1-1]="X"
        print(''.join(str1))
        print(''.join(str2))
        print(''.join(str3))
        if ((str1[0]=="X")and(str1[1]=="X")and(str1[2]=="X"))or((str2[0]=="X")and(str2[1]=="X")and(str2[2]=="X"))or((str3[0]=="X")and(str3[1]=="X")and(str3[2]=="X"))or((str1[0]=="X")and(str2[0]=="X")and(str3[0]=="X"))or((str1[1]=="X")and(str2[1]=="X")and(str3[1]=="X"))or((str1[2]=="X")and(str2[2]=="X")and(str3[2]=="X"))or((str1[0]=="X")and(str2[1]=="X")and(str3[2]=="X"))or((str1[2]=="X")and(str2[1]=="X")and(str3[0]=="X")):
            input("Выиграл 1-й игрок!")
            flag=1
            break
        input("Ход 2-го игрока")
        x2=int(input("Задайте позицию строки нолика (1-3): "))
        y2=int(input("Задайте позицию столбца нолика (1-3): "))
        count+=1
        print(count)
        if x2==1:
            str1[y2-1]='0'
        elif x2==2:
            str2[y2-1]='0'
        else:
            str3[y2-1]='0'
        print(''.join(str1))
        print(''.join(str2))
        print(''.join(str3))
        if ((str1[0]=='0')and(str1[1]=='0')and(str1[2]=='0'))or((str2[0]=='0')and(str2[1]=='0')and(str2[2]=='0'))or((str3[0]=='0')and(str3[1]=='0')and(str3[2]=='0'))or((str1[0]=='0')and(str2[0]=='0')and(str3[0]=='0'))or((str1[1]=='0')and(str2[1]=='0')and(str3[1]=='0'))or((str1[2]=='0')and(str2[2]=='0')and(str3[2]=='0'))or((str1[0]=='0')and(str2[1]=='0')and(str3[2]=='0'))or((str1[2]=='0')and(str2[1]=='0')and(str3[0]=='0')):
            input("Выиграл 2-й игрок!")
            flag=1
            break 