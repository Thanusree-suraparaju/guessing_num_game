# Number Guessing Game 🎯
A beginner Python project built from scratch.

---

## How it works
1. The computer picks a random number between 1 and 100
2. You keep guessing until you find it
3. After each guess you get a hint — **guess higher** or **guess lower**
4. The game ends when you guess correctly

---

## My thought process
- Started with no plan — figured out the game flow step by step
- `if-elif-else` alone wasn't enough — needed a `while` loop to keep the game going
- The loop condition became `while x != guess` — keep going until the player is correct
- `random` is a module — Python can't do everything on its own, you have to `import` it
- Wrote a function whose only job is to pick and `return` a number — nothing else
- `input()` always returns a string — had to wrap it in `int()`
- Hit an infinite loop — "guess higher" printing forever — because `guess` never changed inside the loop
- Fixed it by moving `input()` inside the loop so the guess updates every iteration
- Used `guess = 0` as the starting value so the loop always begins

---

## Concepts used
- Functions and `return`
- `while` loops
- `if-elif-else` conditions
- Importing modules (`random`)
- User input with `int(input())`

---

## What I'd add later
- A guess counter to track how many attempts it took
- Input validation to handle non-integer entries
- Difficulty levels (easy: 1–50, hard: 1–200)

---
