# Instructions :
# Write some code that reads the content of the file (fruits.txt) and
# generates the following output in the command line:
#
# pear
# apple
# orange
# mandarin
# watermelon
# pomegranate


file = open("fruits.txt", "r")
print (file.read())
file.close()