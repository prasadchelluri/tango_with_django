import time
print(time.time())
start = time.time()
def pytrip(a,b,c):
    return(a**2) + (b**2) == (c**2)
val = 1000
for i in range(1,333):
    for j in range(i+1,499):
        k = val - (i+j)
        if(pytrip(i,j,k)):
            print(i,'\n',j,'\n',k)
            print(i*j*k)
end = time.time() - start
print(end)
