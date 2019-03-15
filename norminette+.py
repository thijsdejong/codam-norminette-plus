#!/usr/bin/python
import os
import sys
import urllib

VERSIONFILE = "https://raw.githubusercontent.com/thijsdejong/codam-norminette-plus/master/version"
REPOLINK = 'http://bit.ly/norminette'
UPDATE_FAIL = "\n" + "\033[31m" + "Update:" + "\033[0m "
UPDATE_WARN = "\n" + "\033[33m" + "Update:" + "\033[0m "
__version__ = '19.3.6'

OPERATIONS = (' = ', '++', '--', '+=', '-=', '*=', '/=', '&=', '|=', '^=', '<<=', '>>=', 'if (', 'while (', 'return (', '?')

def update():
    try:
        v = urllib.urlopen(VERSIONFILE)
    except Exception as e:
        print(UPDATE_FAIL + "can't fetch version file: " + e)
    else:
        if (v.getcode() == 200):
            version = v.read().rstrip()
            if (version != __version__):
                print(UPDATE_WARN + "version " + version + " is available, you have version " + __version__ + "\n\t" + "repository: " + REPOLINK)
        else:
            print(UPDATE_FAIL + "can't fetch version file")

def get_files(folder):
    for f in os.listdir(folder):
        if (not f.startswith('.')):
            if os.path.isdir(folder + f):
                get_files(folder + f + "/")
    files = [folder + f for f in os.listdir(folder) if os.path.isfile(folder + f)]
    files.sort()
    for file in files:
        check_file(file)

def double_operation(line):
    c = 0
    if not (line.startswith('/*') or line.startswith('**') or line.startswith('*/')):
        for operation in OPERATIONS:
            if operation in line:
                if c > 0:
                    return 1
                c += 1
    return 0

def check_file(filename):
	if (filename.endswith(".c")):
		print("Norme: " + filename)
		file = open(filename, "r")
		ln = 1
		for line in file:
			if (double_operation(line)):
				print("Error (line " + str(ln) + "): multiple operations")
			ln += 1
	else:
		print_invalid_file(filename)

def print_invalid_file(filename, addition = ""):
	print("Norme: " + addition + filename + "\nWarning: Not a valid file")

def main():
	argv = sys.argv
	arguments = len(argv)
	if (arguments == 1):
		get_files("./")
	else:
		for f in argv[1:]:
			if os.path.isdir(f):
				get_files(f + "/")
			elif os.path.isfile(f):
				check_file(f)
			elif f[0] != "/":
				print_invalid_file(f, "./")
			else:
				print_invalid_file(f)
	update()

if (__name__ == "__main__"):
	main()
