""" Contains the checks for makefiles """
from const import MAKEFILERULES

def is_comment(line):
    """ Checks if a line is a comment """
    return line.startswith('#')

def check_rules(f):
    """ Checks if the makefile hass all the required rules """
    for rule in MAKEFILERULES:
        present = 0
        for line in f:
            if line.startswith(rule):
                present = 1
        if not present:
            print "Error: missing " + rule + " rule"
        f.seek(0)

def check_line_length(f):
    """ Checks if the line is not wider than 80 characters """
    f.replace('\t', '    ')
    l = 1
    for line in f:
        if len(line) > 80 + 1:
            print "Error (line " + str(l) + "): line has " + str(len(line) - 1) + " characters"
        l += 1
    f.seek(0)

def check(filename):
    """ Loops through all lines """
    print "Norme: " + filename
    f = open(filename, "r")
    check_rules(f)
    check_line_length(f)
