import os

with open("string.txt", "r") as f:
  data = f.read()

# Take two substrings
substring_1 = data[:50]
substring_2 = data[50:]

with open("part_1.txt", "w") as f:
  f.write(substring_1)

with open("part_2.txt", "w") as f:
  f.write(substring_2)
