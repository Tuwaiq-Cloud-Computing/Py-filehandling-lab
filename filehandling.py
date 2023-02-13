# Open the file and read its contents into a variable
with open("string.txt", "r") as file:
    filedata = file.read()

# Split the contents of the file into lines using the ',' delimiter
lines = filedata.split(",")

# Extract the first and second lines
firstline = lines[0]
secondline = lines[1]

# Write the first line to a file
with open("part_1.txt", "w") as file1:
    file1.write(firstline)

# Write the second line to a file
with open("part_2.txt", "w") as file2:
    file2.write(secondline)



