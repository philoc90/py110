def swap_name(name):
    split_names = name.split()[::-1]

    split_names = ' '.join(split_names)

    split_names = split_names.split(' ', 1)

    split_names[1] = ' '.join(split_names[1].split()[::-1])


    return f'{split_names[0]}, {split_names[1]}'


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
