#!/usr/bin/python

try:
   fh = open("testfile", "r") # w write, r read
   fh.write("This is my test file for exception handling!!") # cant write because its read
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
