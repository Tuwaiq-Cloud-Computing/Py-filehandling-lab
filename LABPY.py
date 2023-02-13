
py_filehandling = open("string.txt", "r")
fileread=py_filehandling.read()
sp_data=fileread.split(',')

print(sp_data)
py_filehandling.close()


file1 = open('string_1.txt', 'w')
file1.write(sp_data[0])
file1.close()
file2 = open('string_2.txt', 'w')
file2.write(sp_data[1])
file2.close()

