""" Contains the checks and logic to find files """
import os
from const import OPERATIONS

def get_files(folder):
    """ Get every file inside a folder and it's folders recursively """
    try:
        for f in os.listdir(folder):
            if not f.startswith('.'):
                if os.path.isdir(folder + f):
                    get_files(folder + f + "/")
        files = [folder + f for f in os.listdir(folder) if os.path.isfile(folder + f)]
        files.sort()
        for filename in files:
            check_file(filename)
    except OSError:
        pass

def double_operation(line):
    """ Checks for double operations if the line is not a comment """
    c = 0
    if not (line.startswith('/*') or line.startswith('**') or line.startswith('*/')):
        for operation in OPERATIONS:
            if operation in line:
                if c > 0:
                    return 1
                c += 1
    return 0

def check_file(filename):
    """ Runs checks based on file extention """
    if filename.endswith(".c"):
        print "Norme: " + filename
        f = open(filename, "r")
        l = 1
        for line in f:
            if double_operation(line):
                print "Error (line " + str(l) + "): multiple operations"
            l += 1
    else:
        print_invalid_file(filename)

def print_invalid_file(filename):
    """ Prints an invalid file warning """
    addition = "./"
    if filename.startswith("/"):
        addition = ""
    print "Norme: " + addition + filename + "\nWarning: Not a valid file"
