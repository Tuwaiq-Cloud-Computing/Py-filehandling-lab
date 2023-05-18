part_1=open('part-1.txt','x')
part_2=open('part-2.txt','x')
part_1.close()
part_2.close()

file_reads=open('string.txt','r')
cont=file_reads.read()


txpt=cont.split(', ')
print(txpt)

part_1=open('part-1.txt','w')
part_1.write(txpt[0])
part_2=open('part-2.txt','w')
part_2.write(txpt[1])

part_1.close()
part_2.close()
file_reads.close()


print(txpt[0])
print(txpt[1])