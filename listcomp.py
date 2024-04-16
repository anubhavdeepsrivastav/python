l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=len(l1)if(len(l1)<len(l2))else len(l2)
l3=[(l1[i],l2[i]) for i in range(c)]
print(l3)