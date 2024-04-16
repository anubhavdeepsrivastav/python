n=input("enter the string")
w=0
c=0
v=0
d=0
for i in n:
    if i==" ":
        w+=1
    elif(i=="a"or i=="e" or i=="i" or i=="o" or i=="u"):
        v+=1
    elif(i.isdigit()):
        d+=1
    else:
        c+=1
print(f"the number of digit is {d}\nthe number of white space is {w}\nthe number of consonants is {c}\nthe number of vowels is{v}")            

