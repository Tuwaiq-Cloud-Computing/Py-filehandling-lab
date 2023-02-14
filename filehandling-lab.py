


Mydata = open("/Users/rawan/Desktop/string.txt",'r')

data = Mydata.read()
failContent = data.split(",")
#print(mydata)
Mydata.close()


fairstPart=failContent[0]
fairstPart2=failContent[1]


fail1 = open("/Users/rawan/Desktop/part1.txt",'w')
fail1.write(fairstPart)
fail1.close()


fail2 = open("/Users/rawan/Desktop/part2.txt",'w')
fail2.write(fairstPart2)
fail2.close()


