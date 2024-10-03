# file
    # do not forgot to open an close file
    # methods of file opening:
        # Основные режимы открытия файла:
            # 'r' - Чтение файла
            # 'w' - Запись в файл
            # 'a' - Добавление в файл 
            # 'r+' - Чтение и запись
            # 'w+' - Запись с чтением
            # 'a+' - Добавление с чтением 

        # Режимы для работы с бинарными файлами:
            # 'rb' - чтение в бинарном режиме.
            # 'wb' - запись в бинарном режиме.
            # 'ab' - добавление в бинарном режиме.
            # 'r+b', 'w+b', 'a+b' - чтение и запись в бинарном режиме.
my_path = 'files/pytext.txt'

def appendToFile(path):
    file = open(path, 'a') # (path, method)
    user_value = input(str('Enter appended text to file ' + path + ': '))
    file.write(user_value + '\n')

    # close file to avoid memory leak
    file.close

appendToFile(my_path)