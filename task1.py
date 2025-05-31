import random

def choose_word():
    words = ["python", "java", "hello", "ruby", "world", "diamond", "visual", "go", "github", "php"]
    return random.choice(words)

def play_hangman():
    word_to_guess = choose_word()
    word_letters = set(word_to_guess)
    alphabet = set(chr(ord('a') + i) for i in range(26))
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word_to_guess]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
    
    if lives == 0:
        print('You died, sorry. The word was', word_to_guess)
    else:
        print('YAY! You guessed the word', word_to_guess, '!!')

play_hangman()
