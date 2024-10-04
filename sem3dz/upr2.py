def simpleinnumber(n):
   i = 2
   a =[]
   while i * i <= n:
       while n % i == 0:
           a.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       a.append(n)
   return a
n = int(input("Введите число:"))

print(simpleinnumber(n))