list_of_numbers = []

list_of_numbers.append(input("Please enter the first number: "))
list_of_numbers.append(input("Please enter the second number: "))
list_of_numbers.append(input("Please enter the third number: "))
list_of_numbers.append(input("Please enter the fourth number: "))
list_of_numbers.append(input("Please enter the fifth number: "))

number_to_check = input("Please enter the number you would like to look for: ")

if number_to_check in list_of_numbers:
    print(f'{number_to_check} is in {list_of_numbers}')

else:
    print(f'{number_to_check} is not in {list_of_numbers}')
