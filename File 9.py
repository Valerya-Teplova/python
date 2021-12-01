#сортировка списка методом пузырька

from random import randint

li = []
n = 10

for i in range(n):
    li.append(randint(1,99))
print("Исходный список: ",li)

for i in range(n-1):
    for j in range(n-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print("Список с сортировкой: ",li)


