def doub(s):
    out = []
    for i in s:
        out.append(i+""+i)
    return "".join(out)       
x=str(input("Enter a string"))
b=doub(x)
print(b)
