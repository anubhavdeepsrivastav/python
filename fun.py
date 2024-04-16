n=input("enter the string")
l=n.split()
c=0
m=len(l[0])
for i in l:
    if len(i)>c:
        p=i
        c=len(i)
for i in l:
    if m >=len(i):
        m=len(i)
        p1=i
    

print(p)     
print(p1)   

