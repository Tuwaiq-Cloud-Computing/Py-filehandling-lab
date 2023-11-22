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

  string ="C:\\Users\\rana_\\Downloads\\string.txt"

with open(string, "r") as file:
      content = file.read()
print(content)

x= content.split(",")
substrings1= x[0]
substrings2= x[1]
f = open("C:\\Users\\rana_\\Downloads\\part_(1).txt","w")
f.write(substrings1)
f.close()

g = open("C:\\Users\\rana_\\Downloads\\part_(2).txt","w")
g.write(substrings2)
g.close()



## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.


----------------------------------------------------------------

