import random

l = []
for e in range(10):
    e = random.randint(-10, 10)
    l.append(e)

l_unique = list(set(l))
l_unique.sort()


def binary_search(array, val, end, start=0):
    mid = (start + end) // 2

    if start > end:
        return 'Такого элемента нет в списке'

    if val == array[mid]:
        return mid

    if val > array[mid]:
        return binary_search(array, val, end, start=mid + 1)

    if val < array[mid]:
        return binary_search(array, val, end=mid - 1)


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


def selected_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        return array


def merge_sort(a):
    N = len(a) // 2
    l1 = a[:N]
    l2 = a[N:]
    if len(l1) > 1:
        l1 = merge_sort(l1)
    if len(l2) > 1:
        l2 = merge_sort(l2)
    return merge_sorted_lists(l1, l2)


def merge_sorted_lists(a, b):
    l = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
    l += a[i:] + b[j:]
    return l


def quick_sort(a):
    if len(a) < 2:
        return a
    less, eq, grt = [i for i in a if i < a[0]], [i for i in a if i == a[0]], [i for i in a if i > a[0]]
    return quick_sort(less) + eq + quick_sort(grt)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def heap_sort(a):
    pass


a = [9, 1, 8]
for i in range()

# a = [9, 1, 8, 9, 9, -5, 2, 2, 0, -9]
# print(quick_sort(a))

# a = [9, 1, 8, -5, 2, 0, -9]
# print(merge_sort(a))


# a = [0, 2, 5, 8, 9, 12]
# b = [1, 3, 4, 6, 7, 10, 11]
# print(merge_sorted_lists(a, b))

# a = [9, 1, 8, -5, 2, 0, -9]
# insertion_sort(a)

# a = [9, 1, 8, -5, 2, 0, -9]
# bubble_sort(a)
# a = [9, 1, 8, -5, 2, 0, -9]
# selected_sort(a)


def digit_sum(val):
    out = 0
    while val // 10 >= 1:
        e = val % 10
        val = val // 10
        out += e
    print(out + val)

