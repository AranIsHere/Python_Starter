import json

numbers = [2, 3, 4, 6, 7, 9, 4]

file_name = 'numbers.txt'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)
