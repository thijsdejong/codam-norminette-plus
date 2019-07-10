""" Holds all the constants """
# Operations

                 # checks for all single '=' related matches e.g: |=, +=, %=
RE_OPERATIONS = (r'(?<=[\+\-\*\/\%\|\&\^\w\d\s])=(?=[^=])',


                 # Ternary checking will be released when
                 # Thijs fixes his weird ternary operations in 42sh.
                 # Otherwise, this addition would fail all Travis'
                 # builds :)
                 # filename: parser_debug: line: 27, line: 42

                 # matches ternary operators
                 # r'\?(?=[^=])',


                 r'\+\+',
                 r'--',
                 r'<<=',
                 r'>>=',
                 r'if \(',
                 r'while \(',
                 r'return \(')
MAKEFILENAMES = ("GNUmakefile", "makefile", "Makefile")
MAKEFILERULES = ("all:", "$(NAME):", "clean:", "fclean:", "re:")

# Version management
VERSION = '19.7.1'
VERSIONFILE = "https://raw.githubusercontent.com/thijsdejong/codam-norminette-plus/master/version"
UPDATECOMMAND = "norminette+ --update"
