"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

import os
''
base = os.getcwd()

file_location = base + '\\src\\foo.txt'

with open(file_location,'r') as f:
    print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file_location = base + "\\src\\bar.txt"

with open(file_location,'w') as f:
    for i in range(3):
        f.write(f"this is line {i+1}\n")
