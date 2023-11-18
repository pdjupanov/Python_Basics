
word_input = input()
word_input_length = len(word_input)

number = 0

for index in range(0, word_input_length):
    current_letter = word_input[index]

    if current_letter == 'a':
        number = number + 1
    elif current_letter == 'e':
        number = number + 2
    elif current_letter == 'i':
        number = number + 3
    elif current_letter == 'o':
        number = number + 4
    elif current_letter == 'u':
        number = number + 5

print(number)
