# Read from the file and assign it's content to a string
with open("/Users/macbook/Downloads/string.txt", "r") as file:
    Orgin = file.read()
print(Orgin)

# Take two substrings
SplitFile = Orgin.split(",")

substring1 = SplitFile[0]
substring2 = SplitFile[1]

print("The first part is :", substring1)
print("The second part in :", substring2)

# Take each substring and wirte it into a differnt "part_(number).txt" file
with open("part_1.txt", "w") as file:
    file.write(substring1)

with open("part_2.txt", "w") as file:
    file.write(substring2)

# Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string
with open("part_1.txt", "r") as file:
    SubTex1 = file.read()
print(SubTex1)

with open("part_2.txt", "r") as file:
    SubTex2 = file.read()
print(SubTex2)
