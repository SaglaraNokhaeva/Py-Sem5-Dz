# Создайте программу для игры в ""Крестики-нолики"
input("Игра 'Крестики-нолики'. Два игрока поочерёдно делают ход." )
input("" )
str1=HHH
str2=HHH
str3=HHH
print(str1)
print(str2)
print(str3)
flag=0
while flag==0:
    input("Ход 1-го игрока")
    x1=int(input("Задайте позицию строки крестика (1-3): "))
    y1=int(input("Задайте позицию столбца крестика(1-3): "))
    if x1==1:
        str1[y1]='X'
    elif x1==2:
        str2[y1]='X'
    else:
        str3[y1]='X'
    print(str1)
    print(str2)
    print(str3)

    input("Ход 2-го игрока")
    x2=int(input("Задайте позицию строки нолика (1-3): "))
    y2=int(input("Задайте позицию столбца нолика (1-3): "))
    if x2==1:
        str1[y2]='X'
    elif x2==2:
        str2[y2]='X'
    else:
        str3[y2]='X'
    print(str1)
    print(str2)
    print(str3)

