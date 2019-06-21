""" Contains the checks for C files """
import re
from const import RE_OPERATIONS


def remove_singleline_comments(f_content):
    """ gets rid of singleline comments // """
    f_content = re.sub(r'\/\/.*', " ", f_content)

    return f_content


def remove_multiline_comments(f_content):
    """ gets rid of multiline comments /*   */ """
    re_matches = re.findall(r'\/\*[\s\S]*?\*\/', f_content)
    f_content = remove_re_matches(f_content, re_matches)

    return f_content


def remove_strings(f_content):
    """ gets rid of strings in code """
    re_matches = re.findall(r'"[\s\S]*?"', f_content)
    f_content = remove_re_matches(f_content, re_matches)

    return f_content


def remove_re_matches(f_content, re_matches):
    """ removes the re_matches except the newlines """
    replacer = " "

    for match in re_matches:
        newlines = 0
        for char in match:
            if char == "\n":
                newlines += 1
        while newlines > 0:
            replacer += "\n"
            newlines -= 1
        f_content = f_content.replace(match, replacer)

    return f_content


def remove_comments_and_strings(f_content):
    """ gets rid interfering comments and strings """
    f_content = remove_multiline_comments(f_content)
    f_content = remove_singleline_comments(f_content)
    f_content = remove_strings(f_content)

    return f_content


def check_multiple_operations(f_content):
    """ Checks for double operations if the line is not a comment """
    l = 1
    for line in f_content:
        operations = 0
        for operation in RE_OPERATIONS:
            operations += len(re.findall(operation, line))
        if operations > 1:
            print "Error (line " + str(l) + "): multiple operations"
        l += 1


def check(filename):
    """ Loops through all lines """
    print "Norme: " + filename
    f = open(filename, "r")
    f_content = f.read()
    f_content = remove_comments_and_strings(f_content)
    f_content = f_content.split("\n")
    check_multiple_operations(f_content)
