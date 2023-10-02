# бинарные (фотки, видео, музыка и тд)
# текстовые

# чтение - r
# запись - w
# дополнение
# open(путь_до_файла, режим_работы, кодировка)
# абсолютный путь, локальный

file = open("byron.txt", mode="r")
# методы режима для чтения
# .read() - считывает весь текст из файла
# .readlines() - считает каждую строку создавая список строк
# .readline() - считывает строчку за строчкой

# text = file.read()
# text = file.readlines()
# text = file.readline()
# text2 = file.readline()
# print(text)
# print(text2)

file.close()  # закрываем соединение с файлом


file2 = open("new_file.txt", mode="w", encoding="utf-8")

# методы для записи в файл
# .write() - записывает указанный текст в одну строку
# .writelines(список_строк) - принимает список строк и записывает их в файл

# file2.write('Я первая строка\n')
# file2.write('Я вторая строка')
# file2.write(f"""
# sdf
# sdf
# sdf
# """)

# lines = [f'{i} строка\n' for i in range(1, 11)]
# file2.writelines(lines)
# file2.close()

# rb - read bytes
# wb - write bytes

# img = open('nature.jpg', mode="rb")
#
# content = img.read()
# print(content)
# img.close()

# with - контекстный менеджер

with open('nature.jpg', mode="rb") as img:
    content = img.read()
    for i in range(10):
        new_img = open(f'{i}.jpg', mode="wb")
        new_img.write(content)
        new_img.close()

print(img.closed)