
# Hangman Game

This is a simple Hangman game implemented in Python where you have to guess the name of an animal.



- Python 3.x

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/nares10/hangman-game
   ```
   
2. Navigate to the directory containing the `hangman.py` file.

3. Run the game:
   ```
   python hangman.py
   ```

## Gameplay

- The hangman will be displayed progressively as you make incorrect guesses.
- You need to input single letters as guesses.
- If the letter you guessed is in the word, it will be revealed in its correct position(s).
- If you guess the word correctly within the allowed number of guesses, you win!
- If you use up all your guesses without guessing the word correctly, you lose.

## Example Hangman Visuals

```
  +---+
  |   |
      |
      |
      |
      |
=========
```

```
  +---+
  |   |
  O   |
      |
      |
      |
=========
```

```
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
```

```
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
```

```
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
```

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## Author

- Naresh Dewasi
