
Rfile = open('string.txt', 'r')
Result =Rfile.read()
Result =Rfile.close()
#print("File content :")
#print(Result)
#divide the sentence into 2 parts by taking the length / 2 
File1 = Result[:len(Result)//2]
File2 = Result[len(Result)//2]
# write the first half into a new file 
with open('part_1.txt', 'w') as f1:
    f1.write(File1)
# write the second half into a new file 
with open('part_2.txt', 'w') as f2:
     f2.write(File2)
# print the two files 
     print("the first half is :")
     print(File1)
     #f1.close()
     print("the second half is: ")
     print(File2) 
     #f2.close()
