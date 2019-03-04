#!/usr/bin/python
import os
import sys

def get_files():
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	return (files)


def double_operation(line):
	operations = 0

	if (" = " in line):
		operations += 1
	if ("++" in line):
		operations += 1
	if ("--" in line):
		operations += 1
	if ("if (" in line):
		operations += 1
	if ("while (" in line):
		operations += 1
	if ("return (" in line):
		operations += 1
	if ("?" in line):
		operations += 1

	if (operations > 1):
		return (1)
	return (0)

def check_file(filename):
	print("Norme: " + filename)
	if (filename.endswith(".c")):
		file = open(filename, "r")
		ln = 1
		for line in file:
			if (double_operation(line)):
				print("line " + str(ln) + ": multiple operations")
			ln += 1

def main():
	files = get_files()
	for file in files:
		check_file(file)

if (__name__ == "__main__"):
	main()
