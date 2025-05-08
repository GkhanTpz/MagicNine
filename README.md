# ✨ MagicNine

**MagicNine** is a fun little number manipulation project that explores digit shuffling and math patterns in Python!  
It checks if a number contains **different digits**, shuffles them, and performs calculations based on the result.

---

## 🔍 Features

- ✅ Validates if the number has at least two digits and **not all digits are the same**
- 🔀 Shuffles the digits randomly
- ➖ Calculates the **absolute difference** between the original and shuffled number
- 🔢 Displays the **digit sum** of the difference

---

## 🗂️ Project Structure

```

MagicNine/
├── main.py         # Application entry point
└── utils/
├── **init**.py
└── helper.py       # Reusable helper functions

````

---

## ⚙️ Functions Overview (in `utils/helper.py`)

- `digit_count(number)`  
  Returns the number of digits in the given number

- `is_number_valid(number, number_length)`  
  Checks if **at least one digit is different** from the others

- `shuffle_digits(number)`  
  Randomly shuffles the digits of the number

- `digit_sum(number, number_length)`  
  Calculates and prints the **sum of digits**

---

## ▶️ How to Run

Just run the `main.py` file from the root folder:

```bash
python main.py
````

---

## 💡 Example Output

```
Enter a number with at least two digits (at least one digit must be different): 321
The number: 321
Shuffled number: 213
Difference between numbers: 108
Digit sum: 9
```

---

## 📦 Requirements

No third-party libraries needed — just plain old **Python 3.x**.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
