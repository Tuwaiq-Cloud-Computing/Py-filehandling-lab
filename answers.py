

file = "string.txt"
fileContent = open(file,"r")
subStrs = fileContent.read().split(",")

for i in range(len(subStrs)):
	with open(f"part_{i+1}.txt","w+") as f:
		f.write(subStrs[i])
		f.close()

fileContent.close()

