fib = [1,2]
FourMil = 4000000
while fib[-1] < FourMil:
fib.append(fib[1-] + fib[-2])
fib.pop()
print(fib)
evens = [i for i in fib if i%2 == 0]
print(sums(evens))
