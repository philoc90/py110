# Given a dictionary, return its keys sorted by the values associated with each key.

def order_by_value(dict):
    tuples = sorted([(value, key) for (key, value) in dict.items()])
    return [key[1] for key in tuples]


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
