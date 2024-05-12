#THIS is hangman game

#first import random
import random

# Print the intro
print("Welcome to hangman!")


# Ask the player to input a word for the game
chosen_word = input("Enter a word for the game: ").lower()

# Create a list of characters in the word but replace them with _
word_display = ["_" for _ in chosen_word]

# Set the number of wrong attempts allowed so for us its going to be the length of the word they picked
attempts = len(chosen_word)

# Print the intro
print("Welcome to hangman!")

# Game loop
while attempts > 0 and '_' in word_display:
    # Display the current state of the word
    print("\n" + " ".join(word_display))
    
    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is in the chosen word
    if guess in chosen_word:
        # If the guess is correct, reveal the letter(s) in the word display

    #what enumarte does is pairs each character of the chosen word with its 
    #corresponding index. This allows us to keep track of the 
    #position of each letter in the word when comparing it 
    #with the player's guess
        
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the letter in the display
    else:
        # If the guess is incorrect, inform the player and reduce the number of attempts
        print("That letter doesn't appear in the word.")
        attempts -= 1

# Check if the player has guessed all the letters
if "_" not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
    print("You survived the hangman!")
else:
    # If the player has run out of attempts without guessing all the letters, the game ends
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost")















































