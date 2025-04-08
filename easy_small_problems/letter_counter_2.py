# Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.


def word_sizes(words):
    word_frequency = {}
    word_lengths = []

    list_of_words = words.split()

    for word in list_of_words:
        letter_count = 0

        for character in word:

            if character.isalpha():
                letter_count += 1

        word_lengths.append(letter_count)

    for length in word_lengths:
        word_frequency[length] = word_lengths.count(length)

    return word_frequency

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
