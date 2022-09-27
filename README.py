# # Py-filehandling-lab lab-4
# It is time to learn file handling in python!
# - Download the string.txt file
# In python do the following: 
# - Read from the file and assign it's content to a string
# - Take two substrings 
# - Take each substring and wirte it into a differnt "part_(number).txt" file 
# - Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string


file=open("string.txt","r")
mystr=file.read()
lst=mystr.split(",")
file.close()
first=lst[0]
sec=lst[1]



file2=open("part_1.txt","w+")
file2.write(first)
firstOutput=file2.read()
file2.close()

file2=open("part_1.txt","r")
firstOutput=file2.read()
print("fisrt file conent is :" , firstOutput)
file2.close()

file3=open("part_2.txt","w+")
file3.write(sec)
file3.close()

file3=open("part_2.txt","r")
secondOutput=file3.read()
print("Second file conent is :" , secondOutput)
file3.close()




