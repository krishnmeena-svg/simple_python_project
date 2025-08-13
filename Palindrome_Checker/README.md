# 🔄 Palindrome Checker

## 📌 Project Description
A simple Python program that checks whether a given string is a **palindrome**.  
The script removes punctuation and spaces, converts input to lowercase, and then checks if it reads the same forwards and backwards.

**Author:** Krishn Meena

---

## ✨ Features
- Ignores **punctuation** and **spaces** during checking.
- Case-insensitive comparison.
- Works with sentences, phrases, and single words.
- Immediate feedback on whether the input is a palindrome.

---

## 🛠️ Requirements
- Python **3.x**
- No external libraries required (uses built-in `string` module)

---

## 🚀 How to Run
1. Ensure Python 3 is installed on your system.
2. Save the script as:
```bash
palindrome_checker.py
```
3. Open a terminal in the folder containing the script.
4. Run:
```bash
python palindrome_checker.py
```
5. Type the string you want to check when prompted.

---

## 📂 Example Usage

**Example 1 — Palindrome**
```text
type string to check Palindrome- A man, a plan, a canal: Panama
Input String is Palindrome
```
**Example 2 — Not a Palindrome**
```text
type string to check Palindrome- Hello World
Input String is not Palindrome
```
---

## 💡 How It Works
1. Takes user input and converts it to lowercase.
2. Removes all punctuation using `string.punctuation`.
3. Removes spaces from the cleaned string.
4. Compares the string with its reverse.
5. Prints the result.

---

## 📄 License
This project is free to use for learning and educational purposes.

---
