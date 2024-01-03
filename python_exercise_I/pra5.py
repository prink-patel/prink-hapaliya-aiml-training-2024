# Write a Python program that takes a text input and counts 
# the frequency of each word. Display the result in a dictionary format
inp=input("enter text: ")
l=[]
l=inp.split()
wordfreq=[l.count(p) for p in l]

print(dict(zip(l,wordfreq)))
