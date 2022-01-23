from generator_file_docx import generate_file_docx
from generator_file_xslx import generate_file_xslx

while True:
    forman_file = int(input("Введите формат файла для docx - 1, для xlsx - 2 :"))
    if forman_file == 1 or forman_file == 2:
        break
    else:
        print("Вы ввели неверное значение!")

while True:
    unit = str(input("Введите единицу измерения B/Kb/Mb/Gb:"))
    true_variables = ["b", "kb", "mb", "gb"]
    if unit.lower() not in true_variables:
        print("Вы ввели неверное значение!")
    else:
        break

while True:
    try:
        size = int(input("Введите размер файла:"))
        break
    except ValueError:
        print("Введите число!")

while True:
    try:
        count = int(input("Введите нужное количество файлов:"))
        break
    except ValueError:
        print("Введите число!")

while True:
    try:
        step = int(input("Введите шаг в размере между файлами:"))
        break
    except ValueError:
        print("Введите число!")

if forman_file == 1:
    generate_file_docx(size, count, unit, step)
else:
    generate_file_xslx(size, count, unit, step)

input()