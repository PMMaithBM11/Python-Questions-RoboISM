def Convert(string):
    li = list(string.split(" "))
    return li
def listToString(s):     
    str1 = ""  
    for ele in s: 
        str1 += ele  
    return str1     
st = input("Enter string")
data_list =Convert(st)

new_list = []
print(data_list[0])
minimum = data_list[0]  

for x in data_list: 
  if x < minimum:
    minimum = value
    new_list.append(i)
listToString(new_list)
print(new_list)

