# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

data1 = open('text1.txt','r',encoding='UTF-8')
data2 = open('text2.txt','a',encoding='UTF-8')

for s in data1.readlines():
    s=list(s)
    s1=[]
    count=1
    x=len(s)
    for i in range(1,x):
        if s[i]==s[i-1]:
            count+=1
        else:
            s1.append(str(count))
            s1.append(s[i-1])
            count=1
    if s[-1]!=s[-2]:
        s1.append(str(count))
        s1.append(s[x-1])
            
    print(s1)
    data2.write(''.join(s1))
data1.close()
data2.close()