# 🧮 BMI Calculator

This Python script calculates the **Body Mass Index (BMI)** of a person based on their height and weight, and classifies them into categories based on **WHO standards**.

## 📌 Features

- Object-Oriented Programming (OOP) Design
- Proper error handling for invalid inputs
- Follows WHO BMI classification:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Simple and clean output in dictionary format

## 📂 File Structure

```
bmi_calculator.py
README.md
```

## 🚀 How to Run

Make sure you have Python installed (version 3.6+ recommended).

### 🔧 Step-by-step:

1. Clone or download this repository.
2. Open terminal/command prompt in the project folder.
3. Run the script:

```bash
python bmi_calculator.py
```

### ✏️ Sample Output:

```
name: krishn
Body mass index: 22.5
Category: Normal
```

Or if invalid input:

```
error-weight and height must be positive
```

## 🧠 How It Works

The BMI is calculated using the formula:

```
BMI = weight / (height * height)
```

> Height should be in **meters** and weight in **kilograms**.

## 🛠 Example Code

```python
person1 = BMICalculator("Krishn", 65, 1.70)
result = person1.bmi_calculation()

if isinstance(result, dict):
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)
```

## 👨‍💻 Author

**Krishn Meena**  
GitHub: krishnmeena-svg

## 📄 License

This project is licensed under the **MIT License**.
