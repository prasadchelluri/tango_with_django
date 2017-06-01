def prime(n):
    sum,s = 0,[True]*n
    for p in range[2,n]:
        if s[p]:
            sum += 1
            for i in range(p*p,n,p):
                s[i] = False
            if (sum == 10001):
                print(p)
                break
