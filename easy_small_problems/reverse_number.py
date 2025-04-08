def reverse_number(num):
    reversed_number = 0

    while num >= 1:
        reversed_number *= 10
        reversed_number += num % 10
        num //= 10

    return reversed_number

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
