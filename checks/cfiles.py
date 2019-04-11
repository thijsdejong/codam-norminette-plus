""" Contains the checks for C files """
from const import OPERATIONS

def is_comment(line):
    """ Checks if a line is a comment """
    return (line.startswith('/*') or
            line.startswith('**') or
            line.startswith('*/'))

def check_multiple_operations(f):
    """ Checks for double operations if the line is not a comment """
    l = 1
    for line in f:
        operations = 0
        if not is_comment(line):
            for operation in OPERATIONS:
                if operation in line:
                    operations += 1
                    if operations > 1:
                        print "Error (line " + str(l) + "): multiple operations"
        l += 1
    f.seek(0)

def check(filename):
    """ Loops through all lines """
    print "Norme: " + filename
    f = open(filename, "r")
    check_multiple_operations(f)
