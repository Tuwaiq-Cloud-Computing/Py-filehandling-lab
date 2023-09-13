# Read from the file and assign its content to a string
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
# Write substrings to separate files
with open('part_1.txt', 'r') as file:
    part1_content = file.read()
    print("content of part 1 :")
    print(part1_content)
    
with open('part_2.txt', 'r') as file:
    part2_content = file.read()
    print("content of part 2 :")
    print(part2_content)