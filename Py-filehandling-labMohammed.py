with open('string.txt', 'r') as file:
    content = file.read()
# 1. Read from the file and assign its content to a string
with open('string.txt', 'r') as file:
    content = file.read()

# 2. Taking two substrings
# For simplicity, I'm dividing the content into two equal parts.
# If there's another criterion for dividing the content, modify this accordingly.
midpoint = len(content) // 2
substring1 = content[:midpoint]
substring2 = content[midpoint:]

# 3. Writing each substring into different files
with open('part_1.txt', 'w') as file:
    file.write(substring1)

with open('part_2.txt', 'w') as file:
    file.write(substring2)
