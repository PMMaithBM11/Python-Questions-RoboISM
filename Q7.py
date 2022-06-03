
inp = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
 ele = int(input())
  
 inp.append(ele)
print ("Original list : " + str(inp))
max = 0
ans = inp[0]
for i in inp:
    freq = inp.count(i)
    if freq > max:
        max = freq
        ans = i
print ("Most frequent number is : " + str(ans))
