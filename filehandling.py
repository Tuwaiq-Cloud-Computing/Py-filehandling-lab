# Read from the file and assign it's content to a string
# Take two substrings
# Take each substring and wirte it into a differnt "part_(number).txt" file
# Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string

file = open("/Users/abeer./Desktop/string.txt", "r")

mainString = file.read()


string1, string2 = mainString[:len(mainString)//2], mainString[len(mainString)//2:]


file1 = open("/Users/abeer./Desktop/part_1.txt", "w")
file2 = open("/Users/abeer./Desktop/part_2.txt", "w")

file1.write(string1)
file2.write(string2)

file.close()
file1.close()
file2.close()