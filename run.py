""" Runs the norminette+ program """
import os
import sys
from update import check_update, update
from check import get_files, check_file, print_invalid_file
from const import VERSION

def main():
    """ The main function of the program """
    argv = sys.argv
    argc = len(argv)
    option = False
    for arg in argv[1:]:
        if arg.startswith("--"):
            option = True
            if arg == "--update":
                update()
            elif arg == "--version":
                print VERSION
            else:
                print "Invalid option"
    if not option:
        if argc == 1:
            get_files("./")
        else:
            for arg in argv[1:]:
                if os.path.isdir(arg):
                    get_files(arg + "/")
                elif os.path.isfile(arg):
                    check_file(arg)
                else:
                    print_invalid_file(arg)
    check_update()

if __name__ == "__main__":
    main()
