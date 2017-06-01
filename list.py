import random
#list a1
a1 = list(range(101))
#print(a1)

#list a2
a2 = a1[::-1]
#print(a2)

#list a3

#a31 = [random.randint(1,101)for i in range(1,101)]
#randint needs no predefined list
#print(a3)

#a32 = [random.choice(a1) for i in range(1,101)]
#choice() needs a predeficed list and further gives duplicate values
#print(a32)
a3 =  random.sample(a1,100)
f1 = open("test.txt",mode = 'wt')
f1.write(' '.join(str(random.sample(a1,100))))
f2 = open("test.txt",mode="r")
a4 = f2.read()
print("testPrint")
print(a4)
a5 = a4.split()
#print(a5)

def bub_sort(mylist):
    count = 0
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
                if mylist[j]>mylist[j+1]:
                    temp = mylist[j]
                    mylist[j] = mylist[j+1]
                    mylist[j+1] = temp
                    count  = count + 1
    print(count)
print("List A1 After Bubble Sort ")
bub_sort(a1)
print(a1)
print("List A2 after bubble sort")
bub_sort(a2)
print(a2)
print("List A3 after bubble sort")
bub_sort(a3)
print(a3)
#print(a5)
