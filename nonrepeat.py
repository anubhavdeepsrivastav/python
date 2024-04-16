n=int(input("enter the number of caps "))
c=0
m=0
for i in range(1,n+1):
    for j in range(i,n):
        m+=j
        if m>n:
            m=0
            break
        if(m==n):
            c=c+1
            m=0
            break
            

print(c)       
        