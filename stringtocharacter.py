l=[]
c=0
m=0
n=int(input("enter the limit"))
for i in  range(0,n):
    val=int(input("enter the value at index {i}="))
    l.append(val)
for i in range(0,n):
    for i1 in range(i+1,n):
        c+=l[i1]
    m+=l[i]
    if(m==c):
        print(True)
    c=0    