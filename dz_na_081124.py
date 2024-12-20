import time
import matplotlib.pyplot as plt
import numpy as np

def buble(A):
    t_b_o = time.time()
    for j in range(len(A) - 1):
        for i in range(0, len(A)-1-j):
            if not A[i] <= A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
    t_b_1 = time.time()
    t_b = t_b_1 - t_b_o
    return t_b

def selection(A):
    t_s_o = time.time()
    def find_max_i(A):
        res = 0
        for i in range(1, len(A)):
            if A[i] >= A[res]:
                res = i
        return res

    def selection_sort(A):
        for i in range(len(A) - 1):
            j = find_max_i(A[:len(A)-1])
            f = len(A)-i-1
            A[j], A[f] = A[f], A[j]
    selection_sort(A)
    t_s_1 = time.time()
    t_s = t_s_1 - t_s_o
    return t_s

def insortion(A):
    t_i_o = time.time()
    n = len(A)
    for i in range(0,n-1):
        while i>=0 and A[i+1] < A[i]:
            A[i + 1], A[i] = A[i], A[i + 1]
            i = i - 1
    t_i_1 = time.time()
    t_i = t_i_1 - t_i_o
    return t_i

n_array_A=[]
N=[]
TB=[]
TS=[]
TI=[]
TI_bad = []
bad_array_insort=[]
bad_array_insort_i = []
for n in range(1,1000,50):
    rand_arr = np.random.randint(-100, 100, size=n)
    n_array_A.append(rand_arr)
    N.append(n)
    TB.append(buble(rand_arr))
    TS.append(selection(rand_arr))
    TI.append(insortion(rand_arr))
    bad_array_insort_i = sorted(rand_arr, reverse=True)
    bad_array_insort.append(bad_array_insort_i)
    TI_bad.append(insortion(bad_array_insort_i))
w=np.hanning(5)
TB2=np.convolve(w/w.sum(),TB,mode='same')
TS2=np.convolve(w/w.sum(),TS,mode='same')
TI2=np.convolve(w/w.sum(),TI,mode='same')
TI_bad2=np.convolve(w/w.sum(),TI_bad,mode='same')
# plt.plot(N, TB)
plt.plot(N, TB2, label='Пузырик')
# plt.plot(N, TS)
# plt.plot(N, TI)
plt.plot(N, TS2, label='Выбор')
plt.plot(N, TI2, label='Вставки')
plt.plot(N, TI_bad2, label='Вставки для не отсорт. массива')
plt.legend(loc='best')
plt.ylabel("Время сортировки")
plt.xlabel("Размер массива для сортировки")
plt.show()
