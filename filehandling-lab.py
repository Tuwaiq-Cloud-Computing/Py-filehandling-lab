with open("string.txt", "r") as file:
    content = file.read()
    file1 = open("string.txt", "r")
print(file1.read())

substrings = content.split(",")

substring1 = " ".join(substrings[:len(substrings)//2])
substring2 = " ".join(substrings[len(substrings)//2:])

with open("part_1.txt", "w") as file1:
    file1.write(substring1)

with open("part_2.txt", "w") as file2:
    file2.write(substring2) 