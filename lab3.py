def split_and_write_file():
    # Read the content of the file and assign it to a string
    with open('string.txt', 'r') as file:
        content = file.read()
    # Split the string into two substrings
    index = content.find(',') 
    if index != -1:
        substring1 = content[:index]
    # Write each substring to a separate file
    with open('1.txt', 'w') as file1:
        file1.write(substring1)
        print("content of file 1:")
        print(substring1)
        
    substring2 = content[index+1:]
    with open('2.txt', 'w') as file2:
        file2.write(substring2)
        print("content of file 2:")
        print(substring2)
# Call the function to split and write the file
split_and_write_file()

