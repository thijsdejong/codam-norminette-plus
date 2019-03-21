# Norminette+ [![Build Status](https://travis-ci.com/thijsdejong/codam-norminette-plus.svg?branch=master)](https://travis-ci.com/thijsdejong/codam-norminette-plus)
A program created to automatically check the norm rules that `norminette` does not check

## Usage
Run the following command to download norminette+
```
git clone https://github.com/thijsdejong/codam-norminette-plus ~/norminette+
```
Add the following line to your `~/.zshrc`
```
alias norminette+="python ~/norminette+/run.py"
```
To use norminette+ you can run the following command in any folder
```
norminette+
```

## Updating
Norminette+ will give you a notification when you do not have the latest version.
Run the following command to update norminette+
```
git -C ~/norminette+ pull
```

## TODO
- Check Makefile
  - maximum of 80 characters per line (line has x characters)
  - mandatory rules (all, $(NAME), clean, fclean, re)
