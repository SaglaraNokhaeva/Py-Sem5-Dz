# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

data1 = open('text1.txt','r',encoding='UTF-8')
data2 = open('text2.txt','a',encoding='UTF-8')

for s in data1.readlines():
    s=list(s)
    print(s)
    

data1.close()
data2.write(s)
data2.close()




# Задача 2. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество 
# в ней символов и слов.


# data = open('file.txt', 'r', encoding='UTF-8')

# for s in data.readlines():
#     print(s, end='')
#     print(f'Количество символов = {len(s)}')
#     print(f"Количество слов = {len(s.split())}")
#     print()
# data.close()