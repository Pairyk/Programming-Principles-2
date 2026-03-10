import os
import shutil

with open("test.txt", 'w') as file:
    file.write("Terraria is truly a wonderful game, that you should try out!\n")

with open("test.txt", 'r') as file:
    line = file.readline()
    print(line)

with open("test.txt", 'a') as file:
    file.write("Terraria is also available in all platforms!\n")
    shutil.copy("test.txt", "ejudge_6/test.txt")

def file_remove(path):
    if os.path.isfile(path):
        os.remove(path)

file_remove("test.txt")
