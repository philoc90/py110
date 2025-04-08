def digit_list(num):
    list_of_digits = []

    while num >= 1:
        list_of_digits.append((num % 10))
        num //= 10

    list_of_digits.reverse()

    return list_of_digits

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
