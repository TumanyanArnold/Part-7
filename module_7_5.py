import os
import time


directory = 'D:\Personal\Модуль №7. Работа с файлами и форматированный вывод'
count = 0
for root, dirs, file in os.walk(directory):
    for files in file:
        filepath = os.path.join(root, files)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        count += 1
        print(f'Обнаржен файл: {file}\nПуть: {filepath}\nРазмер: {filesize} байт'
            f'\nВремя изменения: {formatted_time}\nРодительская директория: {parent_dir}')
