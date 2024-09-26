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
n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))
mnozhiteli_n1 = simpleinnumber(n1)
mnozhiteli_n2 = simpleinnumber(n2)
print(mnozhiteli_n1, mnozhiteli_n2)
nod = 1
dlina1 = len(mnozhiteli_n1)
dlina2 = len(mnozhiteli_n2)
print(dlina1, dlina2)
if dlina2 >= dlina1:
    for i in range(dlina1):
        if mnozhiteli_n1[i] in mnozhiteli_n2:
            nod *= mnozhiteli_n1[i]
elif dlina1 > dlina2:
    for i in range(dlina2):
        if mnozhiteli_n2[i] in mnozhiteli_n1:
            nod *= mnozhiteli_n2[i]
print(nod)
