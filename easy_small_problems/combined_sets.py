def union(list_one, list_two):
    list_one = set(list_one)
    list_two = set(list_two)

    final_set = list_one | list_two

    return final_set

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
