import math
def fac_num(n):
    #fac = []
    num = 0
    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            num += 2
        else:
            continue

    return num
def tri_num():
    i = 1
    j = 1
    while(True):
        triangle = j
        j = (j+1) + 1
        fac_num(triangle)
        i = i+1
        if (fac_num(triangle) >= 500):
            print(triangle)
            break
tri_num()
#print("Time Taken")
