

# Задание №1

n = int(input("Введите количество чисел в диапазоне от 1 до 100.001: ")) 
while n < 1 or n > 100_000:
    n = int(input("Введите правильный диапазон чисел от 1 до 100.001: "))
if n == 1:
    k = "число"
elif n == 2 or n == 3 or n == 4:
    k = "числа"
else:
    k = "чисел"    
lst = list(map(int, input(f"Введите {n} {k} через пробел, в диапазоне от 1 до 1000000001: ").split()))
while len(lst) != n:
    lst = list(map(int, input(f"Не верное количество чисел! Введите {n} {k} через пробел, в диапазоне от 1 до 1000000001: ").split()))

setlst = set(lst)
setlstlen = len(setlst)

print (f'Количество различных чисел среди данных равно: {setlstlen}')



# Задание №2

lst1 = list(map(int, input(f"Введите до 100.000 чисел через пробел в первый список: ").split()))
lst2 = list(map(int, input(f"Введите до 100.000 чисел через пробел в второй список: ").split()))

m1 = set(lst1)
m2 = set(lst2)
m1m2 = m1.union(m2)

l1l2 = (len(lst1) + len(lst2))
#m1m2 = len(m1) + len(m2)

print (f'Количество чисел содержащихся одновременно как в первом списке, так и во втором равно: {l1l2}')
print (f'Количество уникальных чисел содержащихся одновременно как в первом списке, так и во втором равно: {len(m1m2)}')



# Задание №3

lst = list(map(int, input(f"последовательность чисел через пробел: ").split()))

m = set(lst)

x = len(m)

for i in m:
    if lst.count(i) > 1:
        print (i, "Yes")
    else:
        print (i, "No")      
