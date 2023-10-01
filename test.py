with open('./string.txt', 'r') as file:
      contant= file.read()
      comma_index=contant.find(',')
      if comma_index !=-1:
         substring1 = contant[:comma_index]
         substring2 = contant[comma_index+1:]

with open('part_1.txt', 'w') as file:
        file.write(substring2)

with open('part_1.txt', 'r') as file:
       part1Contant= file.read()
       print("Contant of part_1.txt:")
       print(part1Contant)

with open('part_2.txt', 'r') as file:
     part2Contant= file.read()
     print("Contant of part_2.txt:")
     print(part2Contant)