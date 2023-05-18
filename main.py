file = open("string.txt","w")
file.write("Working hard for something we don't care about is called stress, Working hard for something we love is called passion")
file =open("string.txt","r")
print(file.read())


text= "Working hard for something we don't care about is called stress"
print(text[0:63])

text= "Working hard for something we love is called passion"
print(text[0:63])

file = open("part1.txt","w")
file.write("Working hard for something we don't care about is called stress")

file = open("part2.txt","w")
file.write("Working hard for something we love is called passion")

