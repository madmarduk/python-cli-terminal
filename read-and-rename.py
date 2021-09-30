import os

cur_dir = os.getcwd() # Текущую директорию записывает в переменную

files = os.listdir(cur_dir) # Список файлов в директории записывает в собсна список

for i in files: # для каждого элемента в списке файлов выводит имя файла
    print(i)

while True: #Основной цикл
    print()
    print("Enter R if you would like to rename a file or any other character to quit: ")
    user_input = input() 

    if user_input in 'Rr': #Если пользователь решил переименовать файл, то предлагается написать название файла
        print("Name a file you would like to rename:")
        old_filename = input()
    else:
        quit()

    print("What name would you like for your file?")
    new_filename = input() #Предлагается новое название для файла

    try:
        os.rename(old_filename, new_filename)
        for i in files:
            print(i)
    except: #В случае, если имя оригинального файла не найдено, просто выводит сообщение, после чего основной цикл начинается с начала
        print("Oops, seems like you've made a mistake while writing a name for a file to rename.")
        print("Maybe you forgot to include file's extension?")
