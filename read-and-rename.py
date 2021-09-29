import os

cur_dir = os.getcwd()

files = os.listdir(cur_dir)

for i in files:
    print(i)

while True:
    print()
    print("Enter R if you would like to rename a file or any other character to quit: ")
    user_input = input()

    if user_input in 'Rr':
        print("Name a file you would like to rename:")
        old_filename = input()
    else:
        quit()

    print("What name would you like for your file?")
    new_filename = input()

    try:
        os.rename(old_filename, new_filename)
        for i in files:
            print(i)
    except:
        print("Oops, seems like you've made a mistake while writing a name for a file to rename.")
        print("Maybe you forgot to include file's extension?")
