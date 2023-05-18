fileS = open("string.txt","r") #Read from the file and assign it's content to a string
text = fileS.read()            #Take two substrings
fileparts = text.split(",")    #Take each substring and wirte it into a differnt "part_(number).txt" file
for index, part in enumerate(fileparts): #Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string
        fileN = open(f"./part_{index}.txt","w")
        fileN.write(part)
        fileN.close()
fileS.close() 