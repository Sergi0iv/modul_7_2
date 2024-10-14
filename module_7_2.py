def custom_write(file_name = 'test.txt', strings):
    strings_positions = {}
    number = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        if i not in file_name:
            strings_positions.append(file.tell(), i)
            file.close()
            return


