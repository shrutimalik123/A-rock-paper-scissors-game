# A-rock-paper-scissors-game
A Python Game 

# 🪨📄✂️ Rock, Paper, Scissors - Python Console Game

A simple, command-line implementation of the classic game, Rock, Paper, Scissors, built for Python beginners. This project demonstrates fundamental Python concepts like loops, conditional statements, user input, and the use of the `random` module.

---

## ✨ Features

* **Simple Console Interface:** Play directly in your terminal.
* **Best-of-Three:** The game runs until one player reaches 3 winning rounds.
* **Input Validation:** The game checks to ensure you only enter valid choices (`rock`, `paper`, or `scissors`).

---

## 🚀 How to Play

### 1. Prerequisites

You only need **Python 3** installed on your machine.

### 2. Running the Game

1.  **Save the code:** Save the Python code into a file named `rock.py`.
2.  **Open your terminal/command prompt.**
3.  **Navigate** to the directory where you saved the file.
4.  **Run the script** using the Python interpreter:

    ```bash
    python rock.py
    ```

### 3. Gameplay

1.  The game will start and display the current scores.
2.  It will prompt you to enter your choice: `rock`, `paper`, or `scissors`.
3.  Type your choice and press **Enter**.
4.  The computer will reveal its choice, and the winner of the round will be declared.
5.  The first player to reach **3 wins** is the overall winner!

---

## 💻 Code Structure

The game logic is straightforward and is contained within a single function.

* **`import random`**: Used to allow the computer to randomly select its move.
* **`choices = [...]`**: A list that holds the valid game options.
* **`while score_player < rounds and score_computer < rounds:`**: The main loop that continues the game until a win condition is met.
* **Input Validation Loop**: A nested `while` loop ensures the player enters one of the valid choices.
* **`if/elif/else` blocks**: Used to check the results of the round (Tie, Player Wins, Computer Wins).

---

## 🤝 Next Steps / Challenges for Beginners

Want to make this game even better? Try implementing these simple challenges:

1.  **Change the rules:** Make the game a "best-of-five" instead of a "best-of-three."
2.  **Add a new option:** Introduce "Spock" or "Lizard" (Rock, Paper, Scissors, Lizard, Spock). You'll need to update the `choices` list and the win/loss logic!
3.  **Keep a history:** Create a list to track the winner of every round played.

