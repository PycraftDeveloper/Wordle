# Wordle

This is a recreation of the popular game with the same name, except in Python.

## How to play

The game will randomly select a word from a list of 5-letter words. The player will have 6 attempts to guess the word. After each guess, the game will provide feedback on which letters are correct and in the correct position (green), which letters are correct but in the wrong position (yellow), and which letters are incorrect (gray).

The player wins the game when they guess the correct word.

## Installation

To play the game, you will need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you will also need to install the project dependencies, which can be done using the command:
```
pip install -r requirements.txt
```

Then you can download and extract a copy of the game (The green button that says `<> Code`, then select `Download ZIP` at the bottom of the pop-up).

## Running the game

To run the game, either open and run the program from an IDLE of your choice (for example Python IDLE or Visual Studio Code) or run the command:
```
python "main.py"
```

With the terminal open to the extracted folder on your machine. To check, run the command:
```
ls
```
And ensure 'main.py' is listed!

## Technical bit

This game was initially created in 2023 and was added to GitHub in 2026. The original version of the game used the Python library [Pygame](https://www.pygame.org/news). More recently I have been developing my own multi-media API for Python/Cython/C++ called [Python Multi-Media API (PMMA)](https://github.com/PycraftDeveloper/PMMA) and the two branches of this GitHub repository will serve to compare the game using Pygame and PMMA. Currently PMMA and the PMMA version of the API are still a work in progress, so stay tuned for updates in the future!