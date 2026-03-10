import os
import shutil

os.makedirs('folder/nested_folder/nested_nested_folder')

with os.scandir('folder') as folders:
    for folder in folders:
        print(folder)


def finder(path, extension):
    with os.scandir(path) as folders:
        for thing in folders:
            if thing.is_file() and thing.name.endswith(extension):
                print(thing)
    
    
with os.scandir('folder') as folders:
    for thing in folders:
        if thing.is_file():
            shutil.copy(thing.path, os.path.join('ejudge_6', thing.name))