# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 100 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

input("На столе лежат 100 конфет. Берите за 1 ход не более 28 конфет. Выигрывает тот, кто сделал последний ход")
# Жеребьёвка
s=100
k=int(input ("Для жеребьёвки введите натуральное число: "))
i=randint(0,k)
if i%2==0:
    print("Вы начинаете!")
    count=int(input("Ваш ход: "))
# Случаи если первый ход у игрока
    if count<13:
        s-=count
        my_count=13-count
        print(f"Я беру: {my_count}") 
        s-=my_count
        print(f"Осталось: {s}")
    elif count>13:
        s-=count
        my_count=42-count
        print(f"Я беру: {my_count}") 
        s-=my_count
        print(f"Осталось: {s}")
else:
    print("Я начинаю!")
    s-=13
    print("Осталось 87 конфет")
# Ход игры
while s>0:
    count=int(input("Ваш ход: "))
    while (count<1)or(count>28):
        print("Введите число от 1 до 28") 
        count=int(input("Ваш ход: "))
    s-=count
    my_count=29-count
    print(f"Я беру: {my_count}")
    s-=my_count
    print(f"Осталось: {s}")
# Вывод итога игры
else:
    if 0<my_count<29:
        print ("Вы проиграли")
    else:
        print (f"Я беру: {my_count}")
        print ("Вы выиграли!")

