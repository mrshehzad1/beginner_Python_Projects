import random
words_list = ['sharp', 'low', 'high', 'power', 'sun']
random_gen = random.randint(0, 4)
choosen_word = words_list[random_gen]
guessed_word = str()
counter = 0
word_iterator = 0
while True:
    letter_inp = str(input('Enter letter to Guess Complete Word:\n '))
    if len(letter_inp) > 1:
        print('You Have Entered More than one Letter. Please Enter only one Letter')
        continue
    elif letter_inp is choosen_word[word_iterator]:
        print('You Guessed Right Letter.')
        guessed_word = guessed_word + choosen_word[word_iterator]
        word_iterator = word_iterator + 1
        if word_iterator == len(choosen_word):
            break
        continue
    elif letter_inp != choosen_word[word_iterator]:
        print('You have Guessed Wrong Letter. Try Again')
        print('{} Attempts Remaining.'.format(4-counter))
    counter = counter + 1
    if counter == 5:
        break
print('Word is --->', guessed_word)
