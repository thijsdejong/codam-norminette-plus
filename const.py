""" Holds all the constants """
# Operations
OPERATIONS = (' = ', '++', '--', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
              'if (', 'while (', 'return (')
MAKEFILENAMES = ("GNUmakefile", "makefile", "Makefile")
MAKEFILERULES = ("all:", "$(NAME):", "clean:", "fclean:", "re:")

# Version management
VERSION = '19.4.2'
VERSIONFILE = "https://raw.githubusercontent.com/thijsdejong/codam-norminette-plus/master/version"
UPDATECOMMAND = "norminette+ --update"
