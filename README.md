# Wordle
Wordle is a single-player game, in which a user is required to guess a 5-letter hidden word in 6 attempts. 

## Task
The user makes a first guess (e.g., "Skate").
Print out a progress guide like this; "√××√+".
- "√" Indicates that the letter at that position was guessed correctly.
- "+" indicates that the letter at that position is in the hidden word, but in a different position.
- "×" indicates that the letter at that position is wrong, and isn't in the hidden word.

This process is repeated until the user either guesses the hidden word correctly—in which case, he wins—or exhausts his 6 attempts; thus, losing. 

The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.