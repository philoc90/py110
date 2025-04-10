def unique_sequence(original):
    output = []
    for num in original:
        if num not in output:
            output.append(num)
    return output

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
