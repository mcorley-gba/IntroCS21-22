#File Input.py
#We will experiment with file inputs here.

#Saved in pi_digits.txt is the first 30 decimal places of pi.

#1. Open the file.
#2. Read the entire contents
#3. Do something (print)

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    #more commands here

    
#print(contents.rstrip())

#open keyword needs one argument: filename as a string
#python will look for this file in the same directory as the script.

#file_object is a local python variable where the file contents are located

#with is a keyword that begins a block of code for working with the file and
#it will automatically close the file when the block is complete

#Data is in a sub-directory
with open('data_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

#with open('subdir1/subdir2/subdir3.../pi_digits.txt')
#In MacOS and Linux operating systems, filepaths are given with the forward slash /
#In windows, filepaths are given with a backslash: C:...\my_file.docx
#   If you use the backslash in python, you get an error b/c backslash is special:
#   C:\path\to\my_file.txt

#For python commands -- always use forward slash, even on windows.

#The path 'data_files/pi_digits.txt' is called a relative filepath -- it is given in relation
#to the current file position.

#Python can also take 'absolute filepaths' -- an exact description from the top down of
#where something is on the computer

#Absolute filepaths are normally longer than relative filepaths -- store them in a string
#before giving the open command.

file_path = '/Users/michaelcorley/Movies/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#print(contents)

#to read line by line, we will use for loops:

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

