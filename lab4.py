

read_file = open('string.txt', 'r')
file_content =read_file.read()
# # Take two substrings
substring_part_1 = file_content[:len(file_content)//2]
substring_part_2 = file_content[len(file_content)//2:]
with open('string part 1.txt', 'w') as f:
    f.write(substring_part_1)

with open('string part 2.txt', 'w') as f:
    f.write(substring_part_2)

    print("File content :")
    print(file_content)
    print("")
    print("substring part 1:")

    print(substring_part_1)

    print("")
    print("substring part 2:")
    print(substring_part_2)