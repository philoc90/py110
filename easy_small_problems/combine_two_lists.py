def interleave(list1, list2):
    interleaved = []

    for item in zip(list1, list2):
        interleaved.extend(item)
    return interleaved

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
