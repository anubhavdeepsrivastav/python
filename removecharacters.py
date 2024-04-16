a=input("enter the string")
b=""
for i in a:
    if i.isalpha():
        b+=i
print(b)