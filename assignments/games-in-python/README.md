
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a text-based Hangman game using core Python concepts such as strings, loops, conditionals, and lists. By the end of this assignment, you will create a playable game loop that handles guesses, tracks progress, and determines win/lose outcomes.

## 📝 Tasks

### 🛠️ Build the Hangman Game Loop

#### Description
Create the main game flow for Hangman where a secret word is chosen, the player enters letter guesses, and the game continues until the word is guessed or attempts run out.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of possible words.
- Ask the player to guess one letter at a time.
- Display the current word progress using placeholders (for example: `_ _ _ _`).
- Reduce remaining attempts when the player guesses an incorrect letter.

### 🛠️ Handle Results and Player Feedback

#### Description
Add clear game feedback so players can understand their progress, repeated guesses, and final outcome.

#### Requirements
Completed program should:

- Inform the player when a guessed letter is correct or incorrect.
- Prevent repeated guesses from counting as new attempts.
- End the game with a win message when the full word is revealed.
- End the game with a lose message when attempts reach zero and show the hidden word.
