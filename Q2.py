def maskify(cc):
    str = ''
    for char in cc[:-4]:
        str += '#'
    str += cc[-4:]
    return str
cdno=input("Enter Card No.: ")
a=maskify(cdno)
print(a)
