def oddoccur(arr):
 
    
    r = 0
     
    
    for e in arr:
        
        r = r ^ e
 
    return r
 
# Test array
arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(arr)
 
print("%d" % oddoccur(arr))
