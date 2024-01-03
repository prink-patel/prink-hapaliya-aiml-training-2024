def fac(n):
    if n==1:
        return n 
    else :
        return n*fac(n-1)
n = int(input("enter a number:"))
if n<0:
    print("Sorry, factorial does not exist for negative numbers")
elif n==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of", n ,"is ",fac(n))
