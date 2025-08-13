# 📚 Mini Library Management System

## 📌 Project Description
A simple Python-based **library management system** that lets a user view available and borrowed books, borrow books, and return borrowed books.  
Designed for learning and demonstration purposes, it runs in a CLI (Command Line Interface) environment and ensures input validation.

**Author:** Krishn Meena

---

## ✨ Features
- **View Books**: Displays all available and borrowed books.
- **Borrow Books**: User can borrow a book if it is available.
- **Return Books**: User can return borrowed books.
- **Input Validation**:
  - Handles invalid menu choices.
  - Handles attempts to borrow unavailable or already borrowed books.
  - Handles returning books not currently borrowed.

---

## 🛠️ Requirements
- Python **3.x**
- No external libraries required (uses Python’s standard library only)

---

## 🚀 How to Run
1. Make sure **Python 3** is installed on your system.
2. Save the script as:
```bash
mini_library.py
```
3. Open a terminal or command prompt in the folder containing the script.
4. Run the program:
```bash
python mini_library.py
```
5. Follow the on-screen menu to view, borrow, or return books.

---

## 📂 Example Usage

**Menu:**
```text
📘 choose option for mini library
1.View Books
2.Borrow
3.Return
4.Exit
```

**Example 1 — Viewing Books:**
```text
Available books: b1,b2,b3,b4
Borrowed books: None
```
**Example 2 — Borrowing a Book:**
```text
Type name of book which you want to borrow- b2
✅ user successfully borrowed book b2
```
**Example 3 — Returning a Book:**
```text
Type which book you want to return- b2
✅ user successfully returned book b2
```
## 📄 License
This project is available for **learning and educational purposes**. Free to modify and share.
