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


def split_string_into_parts(filename):
    with open(filename, 'r') as file:
        content = file.read()

    parts = content.split(',')

    for i, part in enumerate(parts):
        part_filename = f"part_{i+1}.txt"
        with open(part_filename, 'w') as part_file:
            part_file.write(part)

        print(f"Created {part_filename} with content: {part.strip()}")
split_string_into_parts("string.txt")

## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.


----------------------------------------------------------------

