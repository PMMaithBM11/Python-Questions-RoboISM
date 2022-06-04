
n=int(input("Enter n:"))

print("Prime numbers:",end=' ')

for r in range(2,n):

    for i in range(2,r):

        if(r%i==0):

            break

    else:

        print(r,end=' ')  
