# Instructions :
# The function that we implemented in the previous exercise checks integer datatypes, but not about floats.
# So, please expand the conditional block so that floats are counted too.


def string_length(mystring):
    try:
        return len(mystring)
    except TypeError:
        return "Sorry integers don't have length"

# Or

def string_length2(mystring):
    if type(mystring) == int:
         return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return  "Sorry, floats don't have length"
    else:
         return len(mystring)

# print(string_length(7))
# print(string_length2(7.0))
# print(string_length("77"))

# print(string_length2(7))
# print(string_length2(7.0))
# print(string_length2("77"))