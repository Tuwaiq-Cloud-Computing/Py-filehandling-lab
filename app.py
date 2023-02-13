
file1 = open("string.txt", "r")
filedata= file1.read()
lines=filedata.split(",")
firstline=lines[0]
secondline=lines[1]
print(firstline)
FirstFile= open("FirstLine.txt" , "w")
FirstFile.write(firstline)
FirstFile.close()
SecondFile= open("SecondLine.txt" , "w")
SecondFile.write(secondline)