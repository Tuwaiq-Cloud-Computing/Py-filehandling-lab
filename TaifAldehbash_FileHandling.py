#File handfling lab
fileA= open("/Users/taifal.qahtani/Desktop/Tuwaiq - Alibaba Cloud Bootcamp/string.txt", "r")
x= fileA.read()
fileA.close()
x1=x[:int(len(x)/2)]
x2=x[int(len(x)/2):]
part_1=open("/Users/taifal.qahtani/Desktop/Tuwaiq - Alibaba Cloud Bootcamp/part_1.txt", "w")
part_2=open("/Users/taifal.qahtani/Desktop/Tuwaiq - Alibaba Cloud Bootcamp/part_2.txt", "w")
part_1.write(x1)
part_2.write(x2)

