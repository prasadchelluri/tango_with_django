import random
A5 = [random.randint(1,20) for i in range(1,21)]
A6 = [random.randint(1,20) for i in range(1,21)]
print(A5)
print(A6)
A5.sort()
A6.sort()
print("After Sorting")
print(A5)
print(A6)
def merge(a,b):
    c = []
    while len(a)!=0 and len(b)!= 0:
        if a[0]<b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c
merged = merge(A5,A6)
print("After Merging")
print(merged)
