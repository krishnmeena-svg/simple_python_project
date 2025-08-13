# 🏔️ Prime Number Triangle

## 📌 Project Overview
This Python script generates **prime numbers** and displays them in a **right-angled triangular pattern**.  
Each row contains **one more prime number than the previous** row.  
The number of primes displayed is based on **user input**.

---

## ✨ Features
- ✅ Checks if a number is **prime**  
- ✅ Validates **user input**  
- ✅ Generates prime numbers **up to the required count**  
- ✅ Displays them in a **right-angled triangular pattern**  

---

## 📂 Example Output
```text
🅿 tell me how many Prime no. you want in right angle pattern? 10

2
3 5
7 11 13
17 19 23 29
```

## 🚀 How to Run
Clone the repository
```bash
git clone https://github.com/krishnmeena-svg/primeno_pattern.git
cd primeno_pattern
```
Run the script
```bash
python main.py
```
Enter how many prime numbers you want in the triangle.

## 🧮 Prime Number Logic
A number n is prime if:

It is greater than 1.

It has no divisors other than 1 and itself.

This program uses:
```bash
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False
```
to check primality efficiently.

## 👨‍💻 Author
Krishn Meena


