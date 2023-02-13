import os

file_part1 = open("part_1.txt", "x")
file_part2 = open("part_2.txt", "x")
file_part1.close()
file_part2.close()

file = open("string.txt", "r")
content = file.read()
parts = content.split(", ")

file_part1 = open("part_1.txt", "a")
file_part1.write(parts[0])

file_part2 = open("part_2.txt", "a")
file_part2.write(parts[1])

file_part1.close()
file_part2.close()
file.close()