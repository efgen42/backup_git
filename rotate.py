#!/usr/bin/python3
import os

BACKUP_DIRECTORY = 'F:\\gitlab'
LISTING_FILE = BACKUP_DIRECTORY + '\\.listing'
L_SOURCE = []
os.chdir(BACKUP_DIRECTORY)

def rotate():
    class FileException(FileNotFoundError): pass
    try:
        if not os.path.isfile(LISTING_FILE):
            raise FileException()
        # Получаем листинг файлов источника
        f = open(LISTING_FILE)
        for line in f:
                #print(line)
                L_SOURCE.append(line.split()[8])
#       print('L_SOURCE = ', L_SOURCE)


        # Получаем листинг файлов получателя
        L_DEST = os.listdir()
        L_DEST.remove('.listing')
#       print('L_DEST = ', L_DEST)

        # Список лишних файлов на получателе
        L_UNIC = list(set(L_DEST) - set(L_SOURCE))
#       print('\n l_UNIC = ', L_UNIC)

        # Ротируем лишние файлы
        if L_SOURCE:    # Если листинг файла источника пустой, не будем ротировать, на всяк
                if L_UNIC:
                        print("В каталоге назначения есть файлы, которых нет у источника. Выполняем ротацию\n")
                        for file in L_UNIC:
                                os.remove(file)
                                print("Удаляю файл ", file)
                else:
                        print("Ротировать нечего. Выход")

    except FileException:
        print(f'Файл {LISTING_FILE} не найден. Ротация не выполнена')
    
if __name__ == "__main__":
    rotate()
