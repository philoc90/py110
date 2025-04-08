def halvsies(list):
    output = [[], []]

    for idx in range(len(list)):
        if idx + 1 <= ((len(list)/2) + 0.5):
            output[0].append(list[idx])
        else:
            output[1].append(list[idx])

    return output

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
