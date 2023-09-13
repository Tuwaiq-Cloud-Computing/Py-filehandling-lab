with open('string.txt', 'r') as file:
    content = file.read()

# Take two substrings
substring1 = content[:len(content)//2]
substring2 = content[len(content)//2:]

# Write substrings to separate files
with open('part_1.txt', 'w') as file:
    file.write(substring1)

with open('part_2.txt', 'w') as file:
    file.write(substring2)