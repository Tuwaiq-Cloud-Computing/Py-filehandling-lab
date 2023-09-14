

fullObject = open("./string.txt","r")

FullString= fullObject.read().split(",")


fullObject.close()
File_1= FullString.open("./part_1.txt","W")
File_1= FullString.write(FullString[0])
File_2= FullString.open("./part_.txt","W")
File_1= FullString.write(FullString[1])

File_1.close()
File_2.close()




    