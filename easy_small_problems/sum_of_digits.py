def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    return sum

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
