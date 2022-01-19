#File_output.py

#Writing to an empty file.

file_name = 'programming.txt'

with open(file_name, 'w') as file_object: #'w' tells python we want to open in 'write' mode
    file_object.write('Programming in Python is great!')

    #We can open files in
    #   'w' - write mode - will create a file if it doesn't already exist.
    #                    - will always erase existing data
    #   'r' - read mode
    #   'a' - append mode - Use with files that already exists.
    #   'r+' - read/write mode

    #Python can only write string data to .txt files.
    #If you want to write numerical data, you have to convert it to a string first.
    #Use: str() --> str(5)

#Write multiple lines:
with open(file_name, 'w') as file_object: #'w' tells python we want to open in 'write' mode
    file_object.write('Programming in Python is great!\n')
    file_object.write('I enjoy programming python!\n')
    #.write() does not automatically insert newlines when it finishes.

with open(file_name, 'a') as file_object:
    file_object.write('Here is a third line.\n')
