import json

file_name = "numbers.txt"

with open(file_name) as file_obj:
    content = json.load(file_obj)

print(content)
