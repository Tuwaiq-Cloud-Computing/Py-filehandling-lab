with open('string.txt', 'r') as file:
    string = file.read()

substring1 = string[0:int(len(string) / 2)]
substring2 = string[int(len(string) / 2):]

with open('part_1.txt', 'w') as file:
    file.write(substring1)

with open('part_2.txt', 'w') as file:
    file.write(substring2)

print("The content of part_1.txt is:")
with open('part_1.txt', 'r') as file:
    print(file.read())

print("The content of part_2.txt is:")
with open('part_2.txt', 'r') as file:
    print(file.read())
