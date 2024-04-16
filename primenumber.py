n=int(input("enter your number"))
for i in range(2,n+1):
    if(n%i == 0 and i!= n):
        print("It is not a prime number")
        break
    if(i == n):
        print("It is a prime number")
    
    
