f=open("abc.txt","w")
L=["hello\n","my dear\n","how are you"]
f.writelines(L)
f.close()
f=open("abc.txt","r")
f1=f.read()
l1=f1.split("\n")
m=len(l1)
print(m)

f.close()
