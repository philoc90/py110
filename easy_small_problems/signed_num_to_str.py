def signed_integer_to_string(num):
    digits = {
     0:'0',
     1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9'
    }

    string = ''

    if num > 0:
        string += '+'
    if num < 0:
        string += '-'
        num = num * -1

    divisor = 1

    while (divisor * 10) < num:
        divisor *= 10

    while divisor >= 1:
        digit = (num // divisor) % 10
        divisor /= 10
        string += digits[digit]

    return string

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
