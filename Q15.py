
 
s = input("Enter String: ")
alp = dig = sp = 0

for i in range(len(s)):
    if(s[i].isalpha()):
        alp = alp + 1
    elif(s[i].isdigit()):
        dig = dig + 1
    else:
        sp = sp + 1
        
print("\nTotal Number of Alphabets in this String :  ", alp)
print("Total Number of Digits in this String :  ", dig)
print("Total Number of Special Characters in this String :  ", sp)
