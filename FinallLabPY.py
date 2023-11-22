# FinallLabPY.py

import os

file_path = "C:\\Users\\Moath\\OneDrive\\سطح المكتب\\FinallPYTHON\\string.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

length = len(content)
midpoint = length // 2

output_directory = "C:\\Users\\Moath\\Desktop\\"
part_1_file_path = os.path.join(output_directory, "part_1.txt")
part_2_file_path = os.path.join(output_directory, "part_2.txt")

# Check if the output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(part_1_file_path, 'w', encoding='utf-8') as part_1_file:
    part_1_file.write(content[:midpoint])

with open(part_2_file_path, 'w', encoding='utf-8') as part_2_file:
    part_2_file.write(content[midpoint:])


print("Script completed successfully.")
print(f"Output files created at: {output_directory}")
