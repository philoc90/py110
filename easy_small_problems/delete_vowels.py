def remove_vowels(original):
    VOWELS = 'AEIOUaeiou'
    new = []
    for word in original:
        no_vowel_string = ''
        for char in word:
            if char not in VOWELS:
                no_vowel_string += char

        new.append(no_vowel_string)

    return new

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
