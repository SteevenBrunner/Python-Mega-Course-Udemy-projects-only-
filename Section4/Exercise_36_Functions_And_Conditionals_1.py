# Instructions :
# In one of the previous exercises we create the following function:
# def string_length(mystring):
#    return len(mystring)
# Calling the function with a string as input will return the length of that string. However, if an integer is passed to the function call like:
# string_length(10)
# that would generate an error since the len()  function doesn't work for integers.
# Your duty is to modify the function so that if an integer is passed as an input, the function should output a message like "Sorry integers don't have length".


def string_length(mystring):
    try:
        return len(mystring)
    except TypeError:
        return "Sorry integers don't have length"

# Or

def string_length2(mystring):
    if type(mystring) == int:
         return "Sorry, integers don't have length"
    else:
         return len(mystring)

# print(string_length(7))
# print(string_length("77"))

# print(string_length2(7))
# print(string_length2("77"))