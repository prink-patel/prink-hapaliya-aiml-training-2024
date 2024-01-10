import re 
s="""Write a regular expression to search digits inside a string
Find the words with exactly 8 letters from the paragraph using regex
Find the numbers starting with 212 from a string.
Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
Replace all special characters with space using regex
Replace the space character that occurs after a word ending with a or r with a newline character
Sample input: area, not a _a2_ roar took 22
Sample output:
area
not a
_a2_ roar
took 22
   8. Split the given input string on one or more repeated sequences of cat using regex
Sample input: firecatlioncatcatcatbearcatcatparrot
Sample output: ['fire', 'lion', 'bear', 'parrot']
  9. Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits. They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
Sample output: ['{{apple-150}}', 'grape-87']"""

arr=re.findall("[\d]+",s)
print(arr)
