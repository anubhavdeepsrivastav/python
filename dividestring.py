n=input("enter the string")
n1=int(input("enter the string"))
l=[]
c=""
m=1
for i in n:
    c+=i
    if m>=n1:
        
        l.append(c) 
        c=""
        m=0

    m+=1
print(l)    