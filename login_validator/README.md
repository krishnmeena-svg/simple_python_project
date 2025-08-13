# 🔐 Login Credential Validator

## 📌 Project Description
This Python script validates **username** and **password** combinations entered as a single comma-separated input.  
It ensures both the username and password meet defined **security and formatting criteria** to help enforce safe account credentials.

**Author:** Krishn Meena

---

## ✨ Features
- Validates username:
  - Cannot be empty (ignores leading and trailing spaces)
  - Cannot contain special characters (`!,@,#,$,%,...`)
- Validates password:
  - Must be at least **8 characters long**
  - No spaces allowed
  - Must have:
    - At least **one uppercase letter**
    - At least **one lowercase letter**
    - At least **one digit**
    - At least **one special character** (from Python's `string.punctuation`)
- Provides **detailed error messages** if validation fails.
- Prints **✅ Valid login credentials** if all checks pass.

---

## 🛠️ Requirements
- Python 3.x  
- No external libraries (uses only Python’s built-in `string` module)

---

## 🚀 How to Run
1. Make sure you have **Python 3 installed** on your system.
2. Save the script as:
```bash
login_cred_checker.py
```
3. Open a terminal or command prompt in the folder containing the file.
4. Run:
```bash
python login_cred_checker.py
```
5. When prompted, enter your username and password separated by a comma.

---

## 📂 Example Usage

**Example 1 (Valid credentials):**
```text
Enter username and password separated by a comma: krishn123, Pa$$word1
✅ valid login credentials
```

**Example 2 (Invalid credentials):**
```text
Enter username and password separated by a comma: john@123, pass
❌ user name can't contain special character
❌ password must be at least 8 characters
❌ password has no upper case character
```

---

## 💡 Validation Rules Summary
| Field     | Rule |
|-----------|------|
| **Username** | Non-empty, no special characters, spaces trimmed |
| **Password** | ≥ 8 chars, no spaces, at least 1 uppercase, 1 lowercase, 1 digit, 1 special char |

---

## 📄 License
This project is free to use for learning purposes.  

---

