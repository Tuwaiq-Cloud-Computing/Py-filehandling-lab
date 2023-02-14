with open('string.txt') as f:
    string = f.readlines()

myString = str(string)

str1 = myString.partition(',')[0]
str2 = myString.partition(',')[2]

f = open("part_1.txt", "w")
f.write(str1)
f.close()

f = open("part_2.txt", "w")
f.write(str2)
f.close()
