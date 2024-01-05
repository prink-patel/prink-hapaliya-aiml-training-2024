

n=11

c=1
a=(n*2)+3


for i in range(a):
    b=n+1
    b=b-i+1
    c=c+i
    z=1
    x=2
        
    p=1
    for j in range(a):

        if j==0 or j==(a-1) or (i==(a//2) and j==(a//2)):
            print(" o",end=" ")

        elif i==0 or i==(a-1) :
            
            print(" 0",end=" ") 

        elif i<=j and j<n+1:
            
            b=b-1
            print(f"{b:2}",end=" ")
            

        elif j==a-c and i<n+1:
            print(f"{c-1:2}",end=" ")
            c=c-1

        elif  i>a//2 and j<a-i:
            print(f"{z:2}",end=" ")
            z=z+1

        elif (i<=j and j<a//2) or (i>=j and j>a//2):
            
            print(f"{p:2}",end=" ")
            p=p+1
        
        else: 
            print("  ",end=" ")
       
    
    print()
