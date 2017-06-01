A1 = [i for i in range(1,100+1)]
#print("**** printing A1 ****")
#print(A1)
A2 = A1[::-1]
#print("**** printing A2 ****")
#print(A2)
f = open("a3.txt","r")
l = f.readline()
a5 = l.split(",")
A4 = list(map(int,a5))
##print(A4)
a5 = [i for i in range(1,100+1)]
print(a5)
#print(type(a5))
a5.sort()
print(a5)
a6 = [i for i in range(101,200+1)]
print(a6)
#print(type(a6))
a6.sort()
print(a6)
