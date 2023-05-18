file = open("/Users/linaalfraidi/Documents/string.txt", "r") 
contant = file.read()
subString = contant.split(", ")

sting1= open("part_1.txt","x")
sting2= open("part_2.txt","x")
sting1.close()
sting2.close()

print(subString)


sting1= open("part_1.txt","w")
sting1.write(subString[0])

sting2= open("part_2.txt","w")
sting2.write(subString[1])

sting1.close()
sting2.close()
file.close()









