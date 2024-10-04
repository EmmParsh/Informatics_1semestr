import numpy as np

M = int(input("dlina stroki: "))
N = int(input("dlina visoti: "))
a = np.array([[None]*M]*N)
n_stolba = 0
n_stroki = 0
shag_po_x = 1
shag_po_y = 0
for i in range(M * N):
    a[n_stroki][n_stolba] = i + 1
    if shag_po_x != 0:
        coordinata_po_x = n_stolba + shag_po_x
    else:
        coordinata_po_x = n_stroki -1 + shag_po_y
    if coordinata_po_x == M or a[n_stroki + shag_po_y][n_stolba + shag_po_x] != None or coordinata_po_x < -1:
        shag_po_x, shag_po_y = -shag_po_y, shag_po_x
    n_stolba += shag_po_x
    n_stroki += shag_po_y
print(a)
for i in range(N):
    a[i] = a[i]*(i+1)
print(a)