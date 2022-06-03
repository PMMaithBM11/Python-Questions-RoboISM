no=[]
n=int(input("Enter no. of numbers in list: "))
i=1
for i in range(n):
    o = int(input()) 
    no.append(o)
    i+=1
s=input("Enter String: ")
if s == "asc" :
    no.sort()
    print(no)    
elif s == "des":
    no.sort(reverse=True)
    print(no)
elif s == "none":
    print(no)
