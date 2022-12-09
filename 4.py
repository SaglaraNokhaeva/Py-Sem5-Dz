# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

data1 = open('text1.txt','r',encoding='UTF-8')
data2 = open('text2.txt','a',encoding='UTF-8')

for s in data1.readlines():
    s=list(s)
    print(s)
    print()
    s1=[]
    # for i in range(1,len(s)):
    #     count=0
    #     while s[i]==s[i-1]:
    #         count+=1
    #         print(count)
    #     s1.append(count)
    #     s1.append(s[i])
# print(s1)
data1.close()
data2.write(s1)
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