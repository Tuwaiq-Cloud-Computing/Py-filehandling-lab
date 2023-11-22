f = open("string.txt", "r")
string=f.read()

# two substrings
sub1 = string[0:int(len(string) / 2)]
sub2 = string[int(len(string) / 2):]

# Write each substring to a separate file
with open('part_1.txt', 'w') as file:
    file.write(sub1)

with open('part_2.txt', 'w') as file:
    file.write(sub2)

# Print the contents of the files
print("The content of part_1.txt is:")
with open('part_1.txt', 'r') as file:
    print(file.read())

print("The content of part_2.txt is:")
with open('part_2.txt', 'r') as file:
    print(file.read())


