text_file = open("file.txt", "r+")
text_file2 = open("file2.txt", "w+")

#read string from file
data = text_file.read()
# Extract substring and write in file2
last = data.split(',')[-1]
text_file2.write(last)

#remove substring from first file 
r=data.replace(last, " ")
print(r)
text_file.seek(0)
text_file.write(r)
text_file.truncate()   

#close file
text_file.close()
text_file2.close()


 
