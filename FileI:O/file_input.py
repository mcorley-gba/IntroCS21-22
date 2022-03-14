'''#File Input.py
#We will experiment with file inputs here.

#Saved in pi_digits.txt is the first 30 decimal places of pi.

#1. Open the file.
#2. Read the entire contents
#3. Do something (print)

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
    #more commands here

    
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

#Make a list from the lines of a file:
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string='' #empty string for storing all first 30 decimal places
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#When python read text tiles all the data is read as string data. Convert using int(), eval(), or float()

#Reading Large Data Files'''

file_path = 'data_files/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]} ...")
print(len(pi_string))

#Is your birthday in pi
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million decimal points of pi!")
else:
    print("Your birthday does not appear in the first million decimal points of pi.")
        

#Python has no limit to how much data it can process at once. The only limits will come from
#Your own system's memory and storage.
