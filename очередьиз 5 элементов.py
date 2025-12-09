from collections import deque
# для задания 2
n = 10
n2 = 99

queuee = deque(range(1, n + 1))

#dla 3 zadania

name = "имя"
#zadanie 4
stack = []

stack.extend([10, 20, 30, 40, 50, 60])
#zadanie 5
n_cubed = n ** 3

stackk = list(range(1, n + 1))
#zadanie 6
text = input("Введите текст: ")

words = text.split()
#zadanie 1
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print("Очередь:", list(queue))

if queue:
    print("Первый элемент очереди:", queue[0])

print("Очередь после просмотра первого элемента:", list(queue))

if queue:
    removed_element = queue.popleft()
    print("Извлеченный элемент:", removed_element)

print("Очередь после извлечения элемента:", list(queue))
print("zadanie 2")
# zadanie 2
print("Изначальная очередь:", list(queuee))

total_sum = 0
print("Элементы по порядку и их сумма:")
while queuee:
    element = queuee.popleft()
    print(element)
    total_sum += element

print("Общая сумма элементов:", total_sum)

queuee.append(n2)
print("Очередь после добавления числа", n2, ":", list(queuee))

print("zadanie 3")

for i in range(1, n + 1):
    queue.append(f"{name} {i}")

print("Изначальная очередь: ", list(queue))

print("Извлечённые элементы: ")
while queue:
    element = queue.popleft()
    print(element)

print("zadanie 4")

print("Стек:", stack)

top_element = stack.pop()
print("Извлеченный элемент:", top_element)

print("Стек после удаления верхнего элемента:", stack)

if stack:
    print("Верхний элемент:", stack[-1])
else:
    print("Стек пустой.")

print("Стек:", stack)

if stack:
    top_element = stack.pop()
    print("Извлеченный элемент:", top_element)

print("Конечный стек:", stack)

print("zadanie 5")

print("Изначальный стек:", stackk)

product = 1
print("Элементы по порядку и их произведение:")
while stackk:
    element = stackk.pop()
    print(element)
    product *= element

print("Произведение элементов:", product)

stackk.append(n_cubed)
print("Стек после добавления n^3:", stackk)

print("zadanie 6")

for word in words:
    stack.append(word)

reversed_words = []


while stack:
    word = stack.pop()
    reversed_words.append(str(word))


print(" ".join(reversed_words))