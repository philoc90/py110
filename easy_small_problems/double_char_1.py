def repeater(str):
    output =''
    for character in str:
        output += character + character

    return output

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
