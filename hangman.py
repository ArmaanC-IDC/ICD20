
import random
def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    num_letters_in_word = len(word)
    index = 0
    while(index < num_letters_in_word):
        letter = word[index]
   
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        index+=1
    return display

def hangman():
    print("Welcome to Hangman!")
    
    target_word = choose_word()
    guessed_letters = ''
    max_attempts = 6
    attempts_left = max_attempts
    hidden_word = display_word(target_word, guessed_letters)
    while True:
        print("Attempts left:", attempts_left)
        print(hidden_word)
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in target_word:
            print("Good guess!")
            guessed_letters += guess    # add the guess to the guessed letters
            hidden_word = display_word(target_word, guessed_letters)
        else:
            print("Incorrect guess. Try again.")
            guessed_letters += guess    # add the guess to the guessed letters
            attempts_left -= 1
        
        if attempts_left > 0 and not '_' in hidden_word:
            print("Congratulations! You guessed the word:", target_word)
            break
        if attempts_left == 0:
            print("Sorry, you ran out of attempts. The word was:", target_word)
            break

hangman()
