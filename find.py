letter = "o"
mystring = "hello World"
mylist = []
for i in mystring:
    mylist.append(i)
    #print(mylist)
count = 0
for i in mylist:
    print(i)
    if i == letter:
        count += 1

    else:
        continue
print("The no.of times the character occured in String is",count)
