# Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

# Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

# You may (and should) use the leading_substrings function you wrote in the previous exercise:

def substrings(string):
    output = []
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i:j+1] != '':
                output.append(string[i:j+1])
    return output

# All of these examples should print True
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
