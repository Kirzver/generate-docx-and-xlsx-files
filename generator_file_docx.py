def generate_file_docx(size, count, unit, step):

    if unit == "B" or unit == "b":
        for i in range(1, count + 1):
            filename = str(i) + ".docx"
            print(filename)
            create_file = open(filename, "w").truncate(size)
            size += step

    elif unit == "Kb" or unit == "kb":
        for i in range(1, count + 1):
            filename = str(i) + ".docx"
            print(filename)
            create_file = open(filename, "w").truncate(1024 * size)
            size += step

    elif unit == "Mb" or unit == "mb":
        for i in range(1, count + 1):
            filename = str(i) + ".docx"
            print(filename)
            create_file = open(filename, "w").truncate(1024 * 1024 * size)
            size += step

    elif unit == "Gb" or unit == "gb":
        for i in range(1, count + 1):
            filename = str(i) + ".docx"
            print(filename)
            create_file = open(filename, "w").truncate(1024 * 1024 * 1024 * size)
            size += step

    print("Готово!")
