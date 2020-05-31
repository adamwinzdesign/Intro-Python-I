"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
openFoo = open('foo.txt', 'r')
readFoo = openFoo.read()
openFoo.close()
print(openFoo)
print(readFoo)

# with open('foo.txt') as openFile:
#   for line in openFile:
#     print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w+') as bar:
  bar.write("Line One!\n")
  bar.write("Line Two!\n")
  bar.write("Line Three!")
  bar.close()

openBar = open('bar.txt', 'r')
readBar = openBar.read()
openBar.close()
print(openBar)
print(readBar)

# Sean used fp as file pointer
fp = open('bar.txt', 'w')
fp.write("""Line 1\nLine 2\nLine 3""")
fp.close()
