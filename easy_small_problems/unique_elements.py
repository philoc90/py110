# From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

def unique_from_first(lst1, lst2):
    uniques = [item for item in lst1 if item not in lst2]

    return set(uniques)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
