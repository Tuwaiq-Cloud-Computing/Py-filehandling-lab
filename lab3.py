import content

file = open("string.txt", "r")
print(file.read())
print(file)
substrings = content.split(",")
substrings1 = substrings[0]
substrings2 = substrings[1]
print(substrings1)
print(substrings2)

with open("part_1.txt", "w") as file:
  file.write(substrings1)

with open("part_2.txt", "w") as file:
  file.write(substrings2)

print("The content of part_1.txt :  ")
with open('part_1.txt', 'r') as file:
  print(file.read())

print("The content of part_2.txt :  ")
with open('part_2.txt', 'r') as file:
  print(file.read())

