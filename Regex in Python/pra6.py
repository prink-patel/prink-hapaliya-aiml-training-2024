# Replace all special characters with space using regex
import re
s="""Write a regular expression prink121@gmail.com to search digits inside a string
Find the words with exactly 8 letters from the paragraph using regex
Find the numbers starting with 212 from a string.
Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
Write a regular expression 21212332dfdfto get only the part of the email before the "@" sign and include the "@" sign
Replace all special characters with space using regex
Replace the space character  that occurs 212gfgfdgafter a word ending with a or r with a newline character
Sample input: area, not a _a2_ roar took 22
Sample output:"""
arr=re.sub("\W"," ",s)
print(arr)