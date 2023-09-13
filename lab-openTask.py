
readfile = open("/Users/shada/Downloads/string.txt","r")
filecontent = readfile.read()

substrings = filecontent.split(',')

for i, substring in enumerate(substrings):
    filename = f'part_{i + 1}.txt'
    part_file= open(filename,"w")
    part_file.write(substring.strip()) 


part_file.close()
readfile.close()