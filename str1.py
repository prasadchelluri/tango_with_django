print("Lower to Upper")
str = "helloWorld"
str_upr  = ""
for ch in str:
    #print(ord(ch))
    if ord(ch) > 95:
        x = ord(ch)
        #print(x)
        x = x - 32
        y = chr(x)
        #print(y)
        str_upr = str_upr + y
    else:
        str_upr = str_upr + chr(x)
        x = ord(ch)
print(str_upr)
