m=int(input("enter the amount you want"))
m-=100
tt=m//2000
m=m%2000
fh=m//500
m=m%500
hh=m//100
hh+=1
print(f"the two thousand rupee notes are{tt}\nthe five hundred rupees notes are{fh}\nthe hundred rupee note are{hh}")