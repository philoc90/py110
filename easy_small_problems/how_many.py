def count_occurences(lst):
    count = {}
    for element in lst:
        count[element] = lst.count(element)

    set = set(lst)

    for element in set:
        print(f'{element} => {count[element]}')
