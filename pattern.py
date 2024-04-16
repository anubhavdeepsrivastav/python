'''
12*
1***
*****'''
'''a=int(input("enter the number"))
for i in range(1,a+1):
    print(" "*(a-i),end=" ")
    print("*"*(2*i-1))    '''
a=12
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))