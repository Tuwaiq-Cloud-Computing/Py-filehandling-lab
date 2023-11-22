#قراءة محتوى الملف
with open('string.txt', 'r') as file:
    content = file.read()

#تقسيم المحتوى الى جزئين بإستخدام الفاصلة للفصل بين المحتوى
split_index = content.index(',')
substring1 = content[:split_index]
substring2 = content[split_index + 1:]

#كتابة الجزء الاول في ملف part_1.txt
with open('part_1.txt', 'w') as file:
    file.write(substring1)

#كتابة الجزء الاول في ملف part_2.txt
with open('part_2.txt', 'w') as file:
    file.write(substring2)