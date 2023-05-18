#Py-filehandling-lab
import io

#Read from the file and assign it's content to a string

with io.open("string.txt", 'r', encoding='utf-8') as f:
    str = f.read()
    f.close
    print(str)

 #Take two substrings
    ind= str.index(',')  
    lstrlen=len(str) 
    str1=str[0:ind]
    str2=str[ind+1:lstrlen]

 #Take each substring and wirte it into a differnt "part_(number).txt" file

with io.open("part_one.txt", 'a', encoding='utf-8') as f1:
    f1.write(str1)
    f1.close()

with io.open("part_two.txt", 'a', encoding='utf-8') as f2:
    f2.write(str2)
    f2.close()
