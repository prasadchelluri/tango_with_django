sum = 2
for number in range(3,2000000):
    prime = True
    for x in range(2,number):
        if number % x == 0:
            prime = False
    if prime:
        sum += number
print ("Sum =",sum)
