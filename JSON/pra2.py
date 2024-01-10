import json
try:
    with open("sample.json", "r") as read:
         data = json.load(read)
except Exception as e:
     print(e)