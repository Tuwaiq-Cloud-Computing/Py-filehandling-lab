file1 = open("part_1.txt","x")
file1.close()

file2 = open("part_2.txt","x")
file2.close()

file=open("pyt.txt","r")
content=file.read()
parts=content.split(", ")

print(parts)

file1=open("part_1.txt", "w")
file1.write(parts[0])

file2=open("part_2.txt", "w")
file2.write(parts[1])

file1.close()
file2.close()
file.close()

print(parts[0])
print(parts[1])



# fileA = open("pyt.txt","w")
# fileA.write('alrasheed')
# fileA.close()


#fileA = open("python.txt","r+")
#print(fileA.())read
#fileA.close()

#with open ("python.txt","a+") as fileA:
    #fileA.write('hello')
    #fileA.seek(0)
    #print(fileA.read())
    #fileA.close()

