# N1
# def visokos(year):
#     if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#         return "YES"
#     return "NO"
# year = int(input())
# print(visokos(year))
#N2
# def triange(a,b,c):
#     if a < 0 or b < 0 or c <0:
#         return "Error: sides cannot be less than 0"
#     else:
#         if a+b>c and b+c>a and a+c>b:
#             return "YES"
#         else: return "NO"
# a = int(input())
# b = int(input())
# c = int(input())
# print(triange(a,b,c))
# N3
# from cmath import sqrt
#
# a = int(input())
# b = int(input())
# c = int(input())
# def kvadr_ur(a,b,c):
#     if a == 0:
#         if b != 0:
#             return -c/b
#         elif b==0 and c!=0:
#             return 'The equation has no solutions'
#         else: return 'The equation has infinite number of solutions'
#     D = b**2 - 4*a*c
#
#     if D<0:
#         return 'The equation has no solutions'
#     elif D==0:
#         return (-b)/2*a
#     else:
#         return (-b+sqrt(D))/2*a, (-b-sqrt(D))/2*a
# print(kvadr_ur(a,b,c))
# N4
# ferz_x = int(input())
# ferz_y = int(input())
# fig_x = int(input())
# fig_y = int(input())
# if ferz_x == fig_x or ferz_y == fig_y or abs(ferz_x - fig_x) == abs(ferz_y - fig_y):
#     print("YES")
# else:
#     print("NO")
# N5
# n = int(input())
# arr = [int(x) for x in input().split()]
# x = int(input())
# count = 0
# for i in range(n):
#     if x == arr[i]:
#         count += 1
# print(count)
#N6
# n = int(input())
# arr = [int(x) for x in input().split()]
# count = 0
# for i in range(n):
#     if arr[i]>0:
#         count += 1
# print(count)
# N7
# n = int(input())
# a = [int(x) for x in input().split()]
# a = a[n-1:]+a[:n-1]
# print(*a)
# N8
# n = int(input())
# arr = [int(x) for x in input().split()]
# maxx = -float("inf")
# for i in range(n):
#     if arr[i]>maxx:
#         maxx = arr[i]
# print(maxx)
# N9
# n = int(input())
# arr = [int(x) for x in input().split()]
# def minimum(a):
#     minn = float("inf")
#     place = -1
#     for i in range(len(a)):
#         if a[i]<minn:
#             minn = a[i]
#             place = i
#     return a[:place]+a[place+1:], minn
#
# a1 = minimum(arr)[0]
# mysorka1 = minimum(arr)[1]
# a2 = minimum(a1)
# mysorka2 = minimum(a1)[1]
# print(mysorka1, mysorka2)