


file_path = "/Users/dalal/Downloads/string.txt"

with open(file_path, 'r') as file1:
    content = file1.read()
print (content)
substrings = content.split(', ', 1)


print (substrings)
output_file_path1 = "/Users/dalal/Downloads/part_1.txt"
output_file_path2 = "/Users/dalal/Downloads/part_2.txt"

with open(output_file_path1, 'w') as file2:
    file2.write(substrings[0])

with open(output_file_path2, 'w') as file3:
    file3.write(substrings[1])
