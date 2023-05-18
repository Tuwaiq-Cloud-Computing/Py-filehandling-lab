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

fileA = open("/Users/amal/Desktop/string.txt")
string= fileA.read()
fileA.close()
s1=string[:int(len(string)/2)]
s2=string[int(len(string)/2):]
part_1=open("/Users/amal/Desktop/part_1.txt")
part_2=open("/Users/amal/Desktop/part_2.txt")
part_1.write(s1)
part_2.write(s2)
part_1.close()
part_2.close()

## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.


----------------------------------------------------------------

