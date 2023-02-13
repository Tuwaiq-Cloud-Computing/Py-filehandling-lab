
Data = open("/Users/remazalghamdi/Desktop/string.txt",'r')
Data2=Data.read()
subStrings=Data2.split(",")
Data.close()

subString1=subStrings[0]
subString2=subStrings[1]

firstfile = open("/Users/remazalghamdi/Desktop/Part_1.txt",'w')
firstfile.write(subString1)
firstfile.close()

secondfile = open("/Users/remazalghamdi/Desktop/Part_2.txt",'w')
secondfile.write(subString2)
secondfile.close()

