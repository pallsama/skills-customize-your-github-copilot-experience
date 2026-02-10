# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You will create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the foundation for your Hangman game by setting up word selection and game state tracking.

#### Requirements
Completed program should:

- Define a list of possible words for the game
- Randomly select a word from the list using the `random` module
- Initialize variables to track guessed letters and remaining attempts


### 🛠️ Implement the Game Loop

#### Description
Build the main game loop that accepts player guesses and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept single letter guesses from the user
- Display current progress using underscores for unguessed letters (e.g., `_ _ a _ _`)
- Track and display the number of incorrect guesses remaining
- Validate input to ensure only single letters are accepted


### 🛠️ Handle Win/Lose Conditions

#### Description
Implement the logic to determine when the game ends and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (win)
- End the game when attempts are exhausted (lose)
- Display a congratulatory message on win
- Display the correct word and a friendly message on lose
