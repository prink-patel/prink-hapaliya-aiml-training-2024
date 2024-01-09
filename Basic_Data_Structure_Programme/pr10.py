# 10. Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity: O(n)

# Sample: [1,0,2,2,0,1,0,1,2,0,0]
# Output: [0,0,0,0,0,1,1,1,2,2,2]

sample=[1,0,2,2,0,1,0,1,2,0,0]
a=sample.count(0)
b=sample.count(1)
c=sample.count(2)
Output=[]
for i in range(len(sample)):
    if i<a:
        Output.append(0)
    elif i<a+b:
        Output.append(1)
    else:
        Output.append(2)
print(Output)