import os
import sys
import time

def typewrite(text=""):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def loading_effect(text=""):
    print(text, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print('\n')

def clear_load(text=""):
    loading_effect(text)
    clear_screen()

def screen_holder(text=""):
    print('\n', end="")
    typewrite(text)
    loading_effect()
    input("Press enter to continue...")
    clear_screen()


if __name__ == "__main__":
    clear_screen()
    loading_effect()
    clear_load()
    typewrite()
    screen_holder()