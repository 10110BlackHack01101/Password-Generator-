#Password-Generator
import random
import time
import sys
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
def rem_lst_lne():
    sys.stdout.write('\x1b[1A')

    sys.stdout.write('\x1b[2K')
def genletter():
    while True:
        choice = input("Which do you want, Letter/Number/Other/Exit: (L/N/O/E) ")
        if choice == "L":
            rem_lst_lne()
            print(random.choice(letters))
            continue
        elif choice == "l":
            rem_lst_lne()
            print(random.choice(letters))
            continue
        elif choice == "N":
            rem_lst_lne()
            print(random.choice(numbers))
            continue
        elif choice == "n":
            rem_lst_lne()
            print(random.choice(numbers))
            continue
        elif choice == "o":
            rem_lst_lne()
            other = input("Enter other: ")
            rem_lst_lne()
            print(other)
            continue
        elif choice == "O":
            rem_lst_lne()
            other = input("Enter other: ")
            rem_lst_lne()
            print(other)
            continue
        elif choice == "E":
            rem_lst_lne()
            return
        elif choice == "e":
            rem_lst_lne()
            return
        else:
            rem_lst_lne()
            input(color.BOLD + color.RED + "Please Enter L/N/O/E to use your own choice use 'O'" + color.RESET)
            rem_lst_lne()
            continue
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

symbols = ["@", "%"]
rem_lst_lne()
input("Welcome to The Password-Generator: Press Enter To Start")
rem_lst_lne()
genletter()
