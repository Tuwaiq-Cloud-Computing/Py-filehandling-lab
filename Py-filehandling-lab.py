file_path = "C:/Users/ALMOTSAFH/Desktop/string/string.txt"

try:
    with open(file_path, "r") as file1:
        content = file1.read()

    substring1 = content[:len(content)//2]
    substring2 = content[len(content)//2:]

 
    with open('part_1.txt', 'w') as part1_file:
        part1_file.write(substring1)

    with open('part_2.txt', 'w') as part2_file:
        part2_file.write(substring2)

    print("Files 'part_1.txt' and 'part_2.txt' created successfully.")
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
    
    


