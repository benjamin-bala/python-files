import random
def random_choice(word):
    return random.randint(0, len(word) - 1)


def split_words(word):
    value = 0
    word_length = len(word)
    random_dash = random_choice(word)
    
    splitted_words = ''
    answer = ''

    while value < word_length:
        if value == random_dash:
            splitted_words += '_'
            answer += word[value]
        else:
            splitted_words += word[value]
        value += 1    
    
    return splitted_words

#words
word_list = ["james", "laptop", "apple", "dog"]
random_word = word_list[random_choice(word_list)]

print('------Hangman-------')
print('Guess the word correct: ', split_words(random_word))

userinput = input('')

if userinput in random_word:
    print('You guessed correct')
else:
    print('You guessed wrong')


