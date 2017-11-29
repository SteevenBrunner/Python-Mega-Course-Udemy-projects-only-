# Instructions :
# Here is a tricky exercise.
#
# 1. Please download the three text files attached in this lecture and put them in a folder.
# The first text file contains the text Content1 . The second contains Content2 and the third Content3 .
#
# 2. You should create a Python script that generates a new text file which should contain
# the content of all three text files. So the generated file should have this content:
#
# Content1
# Content2
# Content3
#
# In other words, your Python script should merge the three text files.
#
# 3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt

import datetime
import glob2

filenames = glob2.glob("*.txt")
merged_file = open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "a")
for filename in filenames:
    with open (filename, "r") as file:
        merged_file.write((file.read()) + "\n")
merged_file.close()