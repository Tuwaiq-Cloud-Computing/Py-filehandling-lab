file_obj = open("string.txt",'r')
file_data = file_obj.read()
data = file_data.split(',')
print(data)
file_obj.close()

#file part 1 
p1 = open('part_1.txt', 'w')
p1.write(data[0])
p1.close()
#file part2 
p2 = open('part_2.txt', 'w')
p2.write(data[1])
p2.close()

