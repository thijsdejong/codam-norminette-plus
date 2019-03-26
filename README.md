# Norminette+ [![Build Status](https://travis-ci.com/thijsdejong/codam-norminette-plus.svg?branch=master)](https://travis-ci.com/thijsdejong/codam-norminette-plus)
A program created to automatically check the norm rules that `norminette` does not check

## Usage
Run the following command to download norminette+
```
git clone https://github.com/thijsdejong/codam-norminette-plus ~/norminette+
```
Run the following command to add the norminette+ alias to `~/.zshrc`
```
echo 'alias norminette+="python ~/norminette+/run.py"' >> ~/.zshrc
```
To use norminette+ you can run the following command in any folder
```
norminette+
```

## Updating
Norminette+ will give you a notification when you do not have the latest version.
Run the following command to update norminette+
```
norminette+ --update
```
Run the following command to see the current version
```
norminette+ --version
```

## TODO
- Check Makefile
  - maximum of 80 characters per line (line has x characters)
  - mandatory rules (all, $(NAME), clean, fclean, re)
