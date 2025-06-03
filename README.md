# Bangles
A classic logic-based number guessing game. Guess the 3-digit number and get clues: Fermi (correct digit, right place), Pico (correct digit, wrong place), Bagels (no correct digits). Use logic and deduction to find the secret number!

## 🕹️ How to Play

- The computer randomly generates a 3-digit number.
- You have **10 attempts** to guess it.
- After each guess, you’ll receive clues:

| Clue   | Meaning                            |
|--------|------------------------------------|
| Fermi  | Correct digit in the correct place |
| Pico   | Correct digit in the wrong place   |
| Bagels| No correct digits                   |

Use these clues to deduce the secret number.

## ▶️ Example

If the secret number is `427` and you guess `123`, the response will be:
- `2` is correct and in the correct position → **Fermi**
- `1` is correct but in the wrong position → **Pico**
- `3` is incorrect → ignored

## 📦 Features

- Random unique 3-digit number generation
- Clue-based feedback (Fermi, Pico, Bagels)
- Input validation (no repeated digits)
- Cross-platform screen clearing
- Help menu and clean UI

## 🚀 Running the Game

Make sure you have Python 3 installed.

```bash
python bagels.py
