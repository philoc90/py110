def staggered_case(string):
    new_string = ''
    counter = 0

    for char in string:
        if char.isalpha():

            if counter % 2 == 0:
                new_string += char.upper()
                counter += 1

            else:
                new_string += char.lower()
                counter +=1
        else:
            new_string += char

    return new_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
