import random
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def pre_order(node):
    if node:
        print(node.key, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.key, end=' ')
        in_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.key, end=' ')

def print_level_order(root):
    if not root:
        print("Дерево пустое.")
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.key, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print()

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current
def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root
def max_depth(node):
    if node is None:
        return 0
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        return max(left_depth, right_depth) + 1
def count_full_nodes(node):
    if node is None:
        return 0
    count = 0
    if node.left is not None and node.right is not None:
        count = 1
    count += count_full_nodes(node.left)
    count += count_full_nodes(node.right)
    return count
def is_symmetric(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.key == tree2.key) and \
           is_symmetric(tree1.left, tree2.right) and \
           is_symmetric(tree1.right, tree2.left)

def is_tree_symmetric(root):
    if root is None:
        return True
    return is_symmetric(root.left, root.right)
if __name__ == "__main__":
    #root = None
    #random_numbers = [random.randint(1, 100) for _ in range(7)]
    #print("Случайные числа для вставки:", random_numbers)

    #for num in random_numbers:
    #    root = insert(root, num)
    #5
    # Симметричное дерево
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.right.right = Node(3)

    # Несимметричное дерево
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(2)
    root2.left.left = Node(3)

    print("Первое дерево симметрично?:", is_tree_symmetric(root1))
    print("Второе дерево симметрично?:", is_tree_symmetric(root2))
    #4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    #5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    print("Количество узлов с обоими потомками:", count_full_nodes(root))
#3
    print("Максимальная глубина дерева:", max_depth(root))
    root = None
    elements = [50, 30, 60, 20, 40, 50, 70]
    for el in elements:
        root = insert(root, el)


    print("Дерево по уровням:")
    print_level_order(root)
    #1
    print("\nОбход дерева: префронтальный (прямой):")
    pre_order(root)
    print("\nОбход дерева: симметричный (In-order):")
    in_order(root)
    print("\nОбход дерева: постфиксный (Обратный):")
    post_order(root)
    print()
    #2
    try:
        to_delete = int(input("Введите элемент для удаления: "))
    except ValueError:
        print("Некорректный ввод.")
        to_delete = None

    if to_delete is not None:
        root = delete_node(root, to_delete)
        print("Дерево после удаления элемента:")
        print_level_order(root)
#4
