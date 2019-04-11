""" Contains the checks and logic to find files """
import os
from const import MAKEFILENAMES
from checks import cfiles, makefiles

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

def check_file(filename):
    """ Runs checks based on file extention """
    if filename.endswith(".c"):
        cfiles.check(filename)
    elif filename.endswith(MAKEFILENAMES):
        makefiles.check(filename)
    else:
        print_invalid_file(filename)

def print_invalid_file(filename):
    """ Prints an invalid file warning """
    addition = "./"
    if filename.startswith("/") or filename.startswith("./"):
        addition = ""
    print "Norme: " + addition + filename + "\nWarning: Not a valid file"
