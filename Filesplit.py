# split the string text into 2 parts
string = open("string.txt", "r")
text = string.read()
substring = text.split(", ")
string.close()

H1 = open("part_1.txt", "a")
H1.write(substring[0])
H1.close()

H2 = open("part_2.txt", "a")
H2.write(substring[1])
H2.close()


# a append
# r read




