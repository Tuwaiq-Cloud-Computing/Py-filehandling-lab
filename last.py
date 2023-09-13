# Read the content of the file into a string
with open('string.txt', 'r') as file:
    content = file.read()
comma_index = content.find(',')
# Define the two substrings
if comma_index != -1:
    # Extract the substring until the first comma
    substring1 = content[:comma_index]
    substring2 = content[comma_index+1:]

# Write the substrings into separate files
with open('part_1.txt', 'w') as file:
    file.write(substring1)

with open('part_2.txt', 'w') as file:
    file.write(substring2)

 # Read and print the contents of the files
with open('part_1.txt', 'r') as file:
    part1_content = file.read()
    print("Content of part_1.txt:")
    print(part1_content)

with open('part_2.txt', 'r') as file:
    part2_content = file.read()
    print("Content of part_2.txt:")
    print(part2_content)
