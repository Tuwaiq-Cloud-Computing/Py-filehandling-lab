
file = open("string.txt", "r")
fileread=file.read()
cont = fileread.split(", ")

Fline=cont[0]
Sline=cont[1]

FFile= open("FLine.txt" , "w")
FFile.write(Fline)
FFile.close
SFile= open("SLine.txt" , "w")
SFile.write(Sline)
SFile.close




