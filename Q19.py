import random
   
   
# generates a four-digit code
def gen_code(): 
    code = []
       
    for i in range(4):
        a = random.randint(0, 9)
        code.append(a)
           
    return code
       
# user input
def inp_code(): 
    inp = input("Enter your four digit guess code: ")
    return inp
   
   
# The game
def Wordle(): 
       
    genCode = gen_code()
    i = 0
       
    while i < 10:
        out = ""
        inpC = [int(c) for c in inp_code()]
           
        if len(inpC) != 4:
            print("Enter only 4 digit number")
            continue
           
        #if inpC == genCode:
             #print("Correct!", genCode)
             #break
               
        for e in inpC:
               
            if e in genCode:
                   
                if inpC.index(e) == genCode.index(e):
                    out+="R"
                else:
                    out+="Y"
            else:
                out+="B"
        print(out)
        if out == "RRRR":
         print("Correct!", genCode)
         break 
        i += 1
    else:    
        print("Game Over !", genCode)    
           
           

Wordle()
