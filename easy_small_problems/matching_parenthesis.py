def is_balanced(str):
    ACCEPTABLE_CHARACTERS = ("'", '"', '{', '}', '[', ']', '(', ')')
    CANNOT_BE_FIRST = ('}', ')', ']')
    CANNOT_BE_LAST = ('{', '(', '[')
    for character in str:
        if character != '(' and character != ')':
            str = str.replace(character, '')

    if str.count('(') == str.count(')'):
        if (str == '') or (str[0] != ')' and str[-1] != '('):
            return True

    return False

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
