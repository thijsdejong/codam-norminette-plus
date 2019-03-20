""" Runs the norminette+ program """
import os
import sys
from update import update
from check import get_files, check_file, print_invalid_file

def main():
    """ The main function of the program """
    argv = sys.argv
    arguments = len(argv)
    if arguments == 1:
        get_files("./")
    else:
        for arg in argv[1:]:
            if os.path.isdir(arg):
                get_files(arg + "/")
            elif os.path.isfile(arg):
                check_file(arg)
            elif arg[0] != "/":
                print_invalid_file(arg, "./")
            else:
                print_invalid_file(arg)
    update()

if __name__ == "__main__":
    main()
