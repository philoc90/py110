# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

def string_to_integer(string):
    number = 0

    for character in string:
        number = (number * 10) + (ord(character) - 48)

    return number

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
