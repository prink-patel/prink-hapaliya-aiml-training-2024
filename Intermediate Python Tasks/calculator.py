class FormulaError(Exception):pass

def parse(x):
    x_list = x.split()
    if len(x_list)!=3:
        print("input invalid please enter three elements")
    n1,op,n2=x_list
    try:
        n1=float(n1)
        n2=float(n2)
    except ValueError:
        print('the first and third input enter number')

    return n1,op,n2

def cal(n1,op,n2):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1*n2
    elif op=='/':
        return n1/n2
    raise FormulaError('{0} if not a valid operator'.format(op))

while True:
    x = input("enter number")
    if x == 'quit':
        break
    n1,op,n2=parse(x)
    result=cal(n1,op,n2)
    print(result)