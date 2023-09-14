#with open("string.txt", "r") as file:
 #   content = file.read()
#print(content)
#########################
#with open("string.txt", "r") as file:
 #   c = file.read()

#s1 = c[0:7]
#s2 = c[8:12]

#print(s1)
#print(s2)
###############
with open("string.txt", "r") as file:
    c1 = file.read()

sub1 = [c1[0:7], c1[8:12]]

for i, sub in enumerate(sub1, 1):
    filename = f"part_{i}.txt"
    with open(filename, "w") as output:
        output.write(sub)