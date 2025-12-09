print("zadanie 1")
X = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]
N = len(X)

# a) Подсчет положительных элементов и сумма первых пяти
positive_count = sum(1 for x in X if x > 0)
sum_first_five = sum(X[:5]) if N >= 5 else sum(X)
minimum_element = min(X)

print("а) Количество положительных элементов:", positive_count)
print("   Сумма первых пяти элементов:", sum_first_five)
print("   Минимальный элемент массива:", minimum_element)

# b) Увеличить в 2 раза все нечетные отрицательные элементы
for i in range(N):
    if X[i] < 0 and X[i] % 2 != 0:
        X[i] *= 2

print("б) Массив после обработки нечетных отрицательных элементов:", X)

# c) Отсортировать по убыванию только четные элементы
even_elements = [x for x in X if x % 2 == 0]
even_elements.sort(reverse=True)

print("в) Четные элементы, отсортированные по убыванию:", even_elements)

print("zadanie 2")

P = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]

index_to_remove = -1
for i, value in enumerate(P):
    if value < 0:
        index_to_remove = i
        break

if index_to_remove != -1:
    del P[index_to_remove]
    print("Массив после удаления первого отрицательного элемента:", P)
else:
    print("Отрицательных элементов в массиве нет. Массив остается без изменений:", P)

print("zadanie 3")
A = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]

A = [x for x in A if x <= 0]

print("Массив после удаления положительных элементов:", A)

print("zadanie 4")

A = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]

result = []

for x in A:
    if x % 5 == 0:
        result.append(100)
    result.append(x)

print("Результат после вставки 100 перед кратными 5:", result)