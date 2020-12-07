# -*- coding: utf-8 -*-
num = int(input('Podaj dowolną liczbę całkowitą do 30: '))
j, i = 1, 1
while i != num:
    for i in range(1, num):
        i += 1
        j = i*j
print(j)
