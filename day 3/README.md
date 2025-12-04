 Python Practice Exercises

This repository contains a simple Python program that demonstrates three basic concepts:

1. Checking if a number is a multiple of 10.
2. Using a `while` loop to count numbers.
3. Creating an input loop that repeats user messages until they type **"quit"**.

---

## 📌 Code Overview

### 1. **Check if a Number Is a Multiple of 10**
The program asks the user for a number and checks whether it is divisible by 10:
```python
user = int(input('enter a number: '))

if user % 10 == 0:
    print("es multiplo")
else:
    print("no es multiplo ")
```
If the remainder of the division by 10 is zero, it prints `es multiplo`, otherwise `no es multiplo`.

---

### 2. **Counting from 0 to 5 with a While Loop**
This loop prints the numbers from 0 to 5:
```python
curren_number = 0

while curren_number <= 5:
    print(curren_number)
    curren_number += 1
```
It increases the counter by one on each iteration.

---

### 3. **Echo Program with "quit" Command**
This part keeps asking the user to type something. It repeats the message back unless the user types **"quit"**:
```python
promtp = 'tell me something and then i will repeat it back to you'
promtp += '\nEnter "quit" to finish que program.>> '
message = ''
while message != "quit":
    message = input(promtp)
    if message != "quit":
        print(message)
```
This demonstrates how to use a *sentinel value* (`"quit"`) to exit a loop.

---

## 🎯 What You Learn
- How to use **modulus (%)** to check divisibility.
- How to structure and control a **while loop**.
- How to work with **user input** and **exit conditions**.
- How loops can repeat actions until certain criteria are met.

---

## 🚀 How to Run
Run the script using Python 3:
```bash
python your_script_name.py
```
Replace `your_script_name.py` with the actual filename.

---

## 💡 Notes
- The program is written for beginners practicing Python basics.
- Feel free to expand this project by adding more exercises or improving input validation.

