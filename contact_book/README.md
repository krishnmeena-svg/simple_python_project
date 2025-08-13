# 📒 Contact Book Application

A simple **console-based Contact Management System** built with Python.  
It allows you to store, search, update, and delete contacts in a user-friendly menu format.

---

## 📌 Features

- ➕ **Add Contact** (with optional Email and Address)
- 📜 **View All Contacts**
- 🔍 **Search Contact** by name (case-insensitive, partial match allowed)
- ✏ **Update Contact** details (Name, Phone Number, Email, Address)
- ❌ **Delete Contact** by name
- 🚪 **Exit Application** gracefully

---

## 🛠 How It Works

- **Class-based Design**: Uses a `Contact` class to store each contact’s details.
- **Input Validation**: Ensures valid phone numbers and handles wrong inputs.
- **Optional Fields**: Email and address can be left blank.
- **Menu Loop**: Continues running until you choose to exit.
- **Readable Output**: Contacts are displayed neatly using a custom `__str__` method.

---


## ▶ How to Run

1. **Clone this repository**:
```bash
  git clone https://github.com/krishnmeena-svg/contact_book.git
```
 2.**Navigate into the project folder**:
```bash
 cd contact_book
```
 3.**Run the application**:
```bash
 python contact_book.py
```
# 💻 Usage Example
```text
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
📘 choose what you want to do with contact book? 2

Name: Krishn
Phone Number: 9876543210
Email: krishn@gmail.com
Address: Jaipur
```
# 📜 License
This project is open-source and free to use.

# ✍ Author
Krishn Meena
