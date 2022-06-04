
opp = {'NORTH': 'SOUTH', 
            'EAST': 'WEST', 
            'SOUTH': 'NORTH', 
            'WEST': 'EAST'}
   
   
def out(inp):
    final = []
       
    for d in range(0, len(inp)):
           
        if final:
           
            if final[-1] == opp[inp[d]]:
                final.pop()
            else:
                final.append(inp[d])
                   
        else:
            final.append(inp[d])
               
    return final
inp=[]
n=int(input("Enter no. of steps: "))
for i in range (n):
    inp.append(input())
print(out(inp))

    
