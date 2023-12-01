def alphabet_position(text):
    """returns values for alphabet in given text"""
    letters = []
    text = text.lower()
    for char in text:
        if 'a' <= char <= 'z':
            letters.append(str(ord(char) - ord('a') + 1))
    result = " ".join(letters).rstrip()
    print(result)


alphabet_position("The sunset sets at twelve o' clock.")
