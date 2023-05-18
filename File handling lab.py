with open(r"C:\Users\walmo\OneDrive\Desktop\Alibaba Cloud bootcamp\string.txt", 'r') as f:
   lines = f.read() 

part1 = lines[0:64]
part2 = lines[65:]

with open(r"C:\Users\walmo\OneDrive\Desktop\Alibaba Cloud bootcamp\Part1.txt", 'w') as f:
   lines = f.write(part1)
with open(r"C:\Users\walmo\OneDrive\Desktop\Alibaba Cloud bootcamp\Part2.txt", 'w') as f:
   lines = f.write(part2)

FileA = open(r"C:\Users\walmo\OneDrive\Desktop\Alibaba Cloud bootcamp\Part1.txt", "r")
print(FileA.read())
FileA.close()

FileB = open(r"C:\Users\walmo\OneDrive\Desktop\Alibaba Cloud bootcamp\Part2.txt", "r")
print(FileB.read())
FileB.close()
