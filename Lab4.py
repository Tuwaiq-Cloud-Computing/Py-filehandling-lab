


file1 = open("/Users/rubaabuhatlah/Desktop/Python/string.txt","r")
content = file1.read()

substrings = content.split(',')

for i, substring in enumerate(substrings):
    filename = f'part_{i + 1}.txt'
    part_file= open(filename,"w")
    part_file.write(substring.strip()) 


part_file.close()
file1.close()

