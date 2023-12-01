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
