def string_to_signed_integer(string):
    digits = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
    }

    number = 0

    for character in string:
        if character in digits:
            number = (number * 10) + digits[character]
    if string[0] == "-":
        number = number * -1

    return number

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
