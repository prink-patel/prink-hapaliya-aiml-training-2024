# Write a Python function to determine whether a given string is a 
# palindrome

str=input("entr a string: ")
if str == str[::-1]:
    print("palindrome string")
else:
    print("not palindrome string")
