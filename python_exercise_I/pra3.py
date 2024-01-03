# Write a Python program to create a dictionary of student 
# names and grades, and count the number of students with grades above 90.
n=int(input("entr number of student:"))
result={}
count=0
for i in range(n):
    print("enter",i,"student details:")
    names = input("enter names: ")
    grades = int(input("enter marks: "))
    result[names]=[grades]
    
for i in result:
    if result[i][0]>90:
        count=count+1

print(count)
