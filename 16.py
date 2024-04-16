n1=input("ente the string ")
c=""
for i in n1:
    if (n1.count(i)<2):
        c+=i
print(c)        