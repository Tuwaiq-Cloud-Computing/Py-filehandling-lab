fileString = "/Users/sarahaldrees/Desktop/Alibaba-BootCamp/string.txt"

# Read from the file and assign it's content to a string
with open(fileString, "r") as file:
    content = file.read()
print(content)

# Take two substrings
substrings = content.split(",")

substring1 = substrings[0]
substring2 = substrings[1]

print("First part:", substring1)
print("Second part:", substring2)

# Take each substring and wirte it into a differnt "part_(number).txt" file
with open("part_1.txt", "w") as file:
    file.write(substring1)

with open("part_2.txt", "w") as file:
    file.write(substring2)

# Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string
with open("part_1.txt", "r") as file:
    content1 = file.read()
print(content1)

with open("part_2.txt", "r") as file:
    content2 = file.read()
print(content2)