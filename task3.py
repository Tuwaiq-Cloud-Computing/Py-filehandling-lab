
#lujean task
F = open("/Users/lujeenalradhi/Downloads/Py-filehandling-lab-main/string.txt",'r')
F2 = F.read()
F.close()
Data=F2.split(",")

part1=open("/Users/lujeenalradhi/Desktop/Part_1.txt",'w')
part1.write(Data[0])
part1.close()
    
part2=open("/Users/lujeenalradhi/Desktop/Part_2.txt",'w')
part2.write(Data[1])
part2.close()   