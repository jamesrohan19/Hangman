# Write your code here
import random

print("H A N G M A N")
# Create a list of words
words = ['python', 'java', 'kotlin', 'javascript']
menu = input('Type "play" to play the game, "exit" to quit: ')


# Ask the player if they want to play or exit
while menu == "play":
    # Choose a random word for the player to guess
    word = random.choice(words)
    word_list = list(word)
    word_copy = word
    dashes = '-' * len(word)
    dashes_list = list(dashes)
    word_set = set()
    attempts = 8

    while attempts != 0:
        print()
        print(''.join(dashes_list))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print('You should input a single letter')
            continue

        if not guess.islower():
            print('It is not an ASCII lowercase letter')
            continue

        # if the modified dashes matches guess then player wins
        if ''.join(dashes_list) == guess:
            print('You guessed the word!')
            print('You survived!')
            break

        if guess in word_list or guess in word_set:
            # checking if the letter is already guessed
            if guess in word_set:
                print('You already typed this letter')
                # attempts -= 1
            else:
                # adding the guess to the respective index in dashes
                for j in range(word.count(guess)):
                    dashes_list[word_list.index(guess)] = word_list[word_list.index(guess)]
                    word_list[word_list.index(guess)] = ''
                    word_set.add(guess)
        else:
            print('No such letter in the word')
            word_set.add(guess)
            attempts -= 1

        if attempts == 0:
            if guess in word_set:
                print('No improvements')
                print('You are hanged!')
            else:
                print('You are hanged!')

    menu = input('Type "play" to play the game, "exit" to quit: ')