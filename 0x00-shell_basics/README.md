# Shell Basics

This repository contains a collection of basic shell scripts written in Bash. These scripts cover fundamental concepts of working with the shell in Unix-like operating systems.

## Table of Contents

1. [Scripts](#scripts)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Scripts

1. `0-current_working_directory`: Prints the absolute path name of the current working directory.

2. `1-listit`: Lists the contents of the current directory.

3. `2-bring_me_home`: Changes the working directory to the user's home directory.

4. `3-listfiles`: Displays the long format of the files in the current directory, including hidden files.

5. `4-listmorefiles`: Displays the long format of the files in the current directory, including hidden files, with user and group IDs displayed numerically.

6. `5-listfilesdigitonly`: Displays the long format of the files in the current directory, with user and group IDs displayed numerically, and with only digits in the user and group ID columns.

7. `6-firstdirectory`: Creates a directory named "holberton" in the /tmp/ directory.

8. `7-movethatfile`: Moves the file "betty" from /tmp/ to /tmp/holberton.

9. `8-firstdelete`: Deletes the file "betty" from /tmp/holberton.

10. `9-firstdirdeletion`: Deletes the "holberton" directory from /tmp.

11. `10-back`: Changes the working directory to the previous one.

12. `11-lists`: Lists all files (including hidden ones) in the current directory and the parent directory, in long format.

13. `12-file_type`: Prints the type of the file named "iamafile" in the /tmp/ directory.

14. `13-symbolic_link`: Creates a symbolic link to /bin/ls, named __ls__.

15. `14-copy_html`: Copies all HTML files from the current directory to the parent directory.

16. `100-lets_move`: Moves all files that start with an uppercase letter to /tmp/u.

17. `101-clean_emacs`: Deletes all files in the current directory that end with the character "~".

18. `102-tree`: Creates the directories "welcome/", "welcome/to/", and "welcome/to/holberton" in the current directory.

## Usage

To use any of the scripts in this repository, simply make the script executable using the `chmod` command, and then run it in the terminal. For example:

```bash
chmod u+x 0-current_working_directory
./0-current_working_directory

