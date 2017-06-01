def title_fun(s):
    print(s)
    str_split = s.split(' ')
    for i in range(len(str_split)):
        res = list(str_split[i])
        val = ord(res[0])
        if val > 96:
            val = val - 32
            res[0] = chr(val)
            str_split[i] = "" . join(res)
    result =  " " . join(str_split)
    print(result)
str = "hello world"
print("***Title****")
print(title_fun(str))
