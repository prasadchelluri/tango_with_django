from random import randint
A3 = [randint(1,100) for i in range(100)]
print("No.of Elements=",len(A3))
print(type(A3))
print(A3)
f = open("a3.txt","w")
str_list = ",".join(map(str,A3))
print(str_list)
f.write(str_list)
f.close
