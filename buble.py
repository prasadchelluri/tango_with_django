from sys import argv
script,filename = argv
l=open(filename)
t=l.readline()
a4=list(map(int,t.split()))
print(a4)
print(sum(a4))
length=len(a4)
count=0
for i in range(length):
    for j in range(length-1):
        if a4[j]>a4[j+1]:
            a4[j],a4[j+1]=a4[j+1],a4[j]
            count += 1
print(a4)
for i in range(length):
    print(a4.count(a4[i]))
print(count)
