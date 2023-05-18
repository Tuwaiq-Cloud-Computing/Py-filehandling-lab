FileA = open("./string.txt", "r")
text = FileA.read()
fileParts = text.split(",")
for index, part in enumerate(fileParts):
    fileN = open(f"./part_{index}.text", "w")
    fileN.write(part)
    fileN.close()
FileA.close()
