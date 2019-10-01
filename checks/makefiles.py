""" Contains the checks for makefiles """
import re
from const import MAKEFILERULES

def is_comment(line):
    """ Checks if a line is a comment """
    return line.startswith('#')

def check_end_newline(f):
    """ Checks if the makefile ends on one empty line """
    endlines = re.search(r"\n*$", f.read()).group()
    if endlines.count('\n') != 1:
        print "Error: file must end with a single empty line"
    f.seek(0)

def check_rules(f):
    """ Checks if the makefile has all the required rules """
    for rule in MAKEFILERULES:
        present = 0
        for line in f:
            if line.startswith(rule):
                present = 1
        if not present:
            print "Error: missing " + rule + " rule"
        f.seek(0)

def check_line_format(f):
    """ Checks if the line is not wider than 80 characters and does not have trailing spaces """
    l = 1
    for line in f:
        line = line.replace('\t', '    ')
        if len(line) > 80 + 1:
            print "Error (line " + str(l) + "): line has " + str(len(line) - 1) + " characters"
        if line.endswith(" \n"):
            print "Error (line " + str(l) + "): spaces at the end of line"
        l += 1
    f.seek(0)

def check(filename):
    """ Loops through all lines """
    print "Norme: " + filename
    f = open(filename, "r")
    check_end_newline(f)
    check_rules(f)
    check_line_format(f)
