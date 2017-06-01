A1 = [i for i in range(1,100+1)]
print(A1)
A2 = A1[::-1]
f = open("a3.txt","r")
l = f.readline()
a5 = l.split(",")
A4 = list(map(int,a5))
def bubblesort(l):
    length = len(l)
    ctr=0
    swapped = True
    while swapped:
        swapped = False
        for i in range (length-1):
            if l[i] > l[i+1]:
                l[i],l[i+1]  = l[i+1],l[i]
                swapped = True
                ctr +=1
    print(ctr)
    return l
print (bubblesort(A1))
print (bubblesort(A2))
print (bubblesort(A4))
