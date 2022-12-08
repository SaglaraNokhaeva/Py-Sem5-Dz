# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

input_str = input("введите строку: ")
list = (lambda x: x.split('абв'))(input_str)
res=''.join(list)
print (res)