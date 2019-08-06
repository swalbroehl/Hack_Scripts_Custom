#!/usr/bin/env python
import sys
sys.path.append("C:\dev\sulley")
from sulley import *

s_initialize("PLS")


# Use s_static, s_string, s_ and s_delim where appropriate
# Refer to course material for examples and reference for each function

s_static("[playlist]\n")
s_static("NumberOfEntries=")
s_short(1, format="string")
s_static("\n")
s_static("Version=2")
s_static("\n")
s_static("File1")
s_delim("=")
s_string("magic0.mp3")

s_static("\n")

print "Total Mutations: " + str(s_num_mutations())
i=0
while s_mutate():
	fh = open("pls-fuzz\plscase-%i.pls"%i, "w")
	fh.write(s_render())
	fh.close()
	i = i+1
print "Done"
