file1 = open("part_1.txt", "x")

file1.close()

file2 = open("part_2.txt", "x")

file2.close()


fileX = open("string.txt", "r")

Text= fileX.read()

lines = Text.split(", ")

print(lines)



file1 = open("part_1.txt", "w")

file1.write(lines[0])

file1 = open("part_1.txt", "w")

file1.write(lines[1])


file1.close()

file2.close()

fileX.close()

print(lines[0])
print(lines[1])


