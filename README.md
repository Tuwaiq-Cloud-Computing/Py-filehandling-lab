# Py-filehandling-lab 
It is time to learn file handling in python!


## Setup:


- Download the string.txt file


## Tasks:


In python do the following: 
- Read from the file and assign it's content to a string
- Take two substrings 
- Take each substring and wirte it into a differnt "part_(number).txt" file 
- Output: part_1.txt, part_2.txt, each one having a different part (substring) of the string
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

with io.open("part_1one.txt", 'a', encoding='utf-8') as f1:
    f1.write(str1)
    f1.close()

with io.open("part_1two.txt", 'a', encoding='utf-8') as f2:
    f2.write(str2)
    f2.close()



## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.


----------------------------------------------------------------

