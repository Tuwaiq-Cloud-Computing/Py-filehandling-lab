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


## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.


----------------------------------------------------------------

# Read from the file and assign its content to a string
with open("string.txt", "r") as f:
    content = f.read()

# Define the two substrings
substring1 = content[:29]  # "Working hard for something we"
substring2 = content[30:]  # "care about is called stress, Working hard for something we love is called passion."

# Write each substring to a different file
with open("part_1.txt", "w") as f:
    f.write(substring1)

with open("part_2.txt", "w") as f:
    f.write(substring2)

