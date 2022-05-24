# Реализовать программу, получающую на вход строку, состоящую из слов, 
# разделенных пробелами и возвращающую длину каждого слова. 
# Пример: "Солнце небо воздух земля" --> 6 4 6 5

# my_string = 'Солнце небо воздух земля вода'.split(' ')
# print(my_string)
# temp = []
# res = [temp.append(len(i)) for i in my_string]
# print(temp)

my_string = 'Солнце небо воздух земля вода'.split(' ')
print(my_string)
res = list(map(lambda i: len(i), my_string))
print(res)

