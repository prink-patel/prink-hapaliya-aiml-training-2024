# Write a Python program to extract the year, month, date and time 
# using Lambda. Input: 2020-01-15 09:03:32.744178
a="2020-01-15 09:03:32.744178"
b = lambda a: a.split()
c = lambda a:a.split('-')
print(c(b(a)[0]),b(a)[1])