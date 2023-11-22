import os

file_path = os.path.expanduser("~/Desktop/finalPy/string.txt")

with open(file_path, 'r') as file:
    content = file.read()

length = len(content)
midpoint = length // 2

part_1_file_path = os.path.expanduser("~/Desktop/finalPy/part_1.txt")
part_2_file_path = os.path.expanduser("~/Desktop/finalPy/part_2.txt")

with open(part_1_file_path, 'w') as part_1_file:
    part_1_file.write(content[:midpoint])

with open(part_2_file_path, 'w') as part_2_file:
    part_2_file.write(content[midpoint:])

print("Substrings written to part_1.txt and part_2.txt successfully.")