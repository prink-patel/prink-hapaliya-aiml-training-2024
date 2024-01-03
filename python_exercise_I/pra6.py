# Write a Python function that takes a sequence of numbers 
# and determines whether all the numbers are different from each other.
def che(a):
    cout=0
    for i in a:
        if a.count(i)!=1:
            print("same number in list")
            cout=cout+1
            break
    if cout==0:
        print("number is different")
a=[1,2,3,1,5,6]
che(a)