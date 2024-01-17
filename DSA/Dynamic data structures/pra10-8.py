def check(a):
    result={}
    b=set(a)
    if len(a)%2==0:
        return "yes"
    else:
        for i in a:
            if i in result:
                return "Yes"
            else:
                result[i]=1
        else:
            return "No"
n = int(input())
for _ in range(n):
    array = list(map(int,input().split()))
    print(check(array))



            
        

