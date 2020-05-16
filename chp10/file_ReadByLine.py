file_name = 'file_lines.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
