import time
import matplotlib.pyplot as plt
import numpy as np


def merge(A, B):
    i, j, itog = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            itog.append(A[i])
            i += 1
        else:
            itog.append(B[j])
            j += 1
    itog += A[i:] + B[j:]
    return itog


def mergesort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2
    return merge(mergesort(A[mid:]), mergesort(A[:mid]))


def qsort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left >= right:
        return
    i, j = left, right
    pivot = A[left]
    while i <= j:
        while i <= right and A[i] < pivot:
            i += 1
        while j >= left and A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, left, j)
    qsort(A, i, right)


def heap_add(A, value):
    A.append(value)
    i = len(A) - 1
    while i > 0 and A[i] > A[(i - 1) // 2]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2


def heap_pop(A):
    if not A:
        raise IndexError("Heap is empty")
    res = A[0]
    A[0] = A.pop() if len(A) > 1 else A[0]
    i, j = 0, 1
    while j < len(A):
        if j + 1 < len(A) and A[j + 1] > A[j]:
            j += 1
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
            j = 2 * i + 1
        else:
            break
    return res


def heap_sort(A):
    heap = []
    for element in A:
        heap_add(heap, element)
    for i in range(len(A)):
        A[len(A) - i - 1] = heap_pop(heap)


N = []
TM = []
TQ = []
TH = []

for n in range(1, 1000, 50):
    N.append(n)  # Заполняем список N
    rand_arr = np.random.randint(-100, 100, size=n)

    start_time = time.time()
    mergesort(rand_arr.copy())
    TM.append(time.time() - start_time)

    start_time = time.time()
    qsort(rand_arr.copy())
    TQ.append(time.time() - start_time)

    start_time = time.time()
    heap_sort(rand_arr.copy())
    TH.append(time.time() - start_time)

plt.plot(N, TM, label='Merge Sort')
plt.plot(N, TQ, label='Quick Sort')
plt.plot(N, TH, label='Heap Sort')
plt.xlabel("Размер массива")
plt.ylabel("Время сортировки")
plt.legend()
plt.title("Время сортировки в зависимости от размера массива")
plt.show()

