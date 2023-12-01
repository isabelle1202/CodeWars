# What's in a name?
# ...Or rather, what's a name in? For us, a particular string is where we are looking for a name.

# Task
# Write a function, taking two strings in parameter, that tests whether or not the first string contains all of the letters of the second string, in order.

# The function should return true if that is the case, and else false. Letter comparison should be case-INsensitive.


def name_in_str(strng: str, name: str) -> bool:
    name_index = 0
    strng = strng.lower()
    name = name.lower()
    for letter in strng:
        if letter == name[name_index]:
            name_index += 1
            if name_index == len(name):
                return True
    return False


name_in_str("Across the rivers", "chris")
