
with open('string.txt', 'r') as file:
    
    content = file.read()

file1 = content[:len(content)//2]
file2 = content[len(content)//2:]

with open('part_1.txt', 'w') as file:
    file.write(file1)
    
with open('part_2.txt', 'w') as file:
    file.write(file2)      
       
file.close()    
