# Instructions :
# Please take a look at the following code:
#
# temperatures=[10,-20,-289,100]
# def c_to_f(c):
#     if c< -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f=c*9/5+32
#         return f
# for t in temperatures:
#     print(c_to_f(t))
# The code prints out the output of the c_to_f  function multiple times in the terminal.
#
# For this exercise, please write the output in a text file instead of printing it out in the terminal.
#
# The text file content will look like this:
#
# 50.0
# -4.0
# 212.0
#
# Please don't write any message in the text file when input is lower than -273.15.


temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return f
with open ("temperature.txt", "a") as file:
    for t in temperatures:
        f = c_to_f(t)
        if type(f) != str:
            file.write(str(f) + "\n");