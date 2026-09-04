# Python Loops: Hands-On Practice Checklist

## 1. Even or Odd Checker

Write a program to check whether a given integer is **even or odd**.

Then extend the program using a `for` loop to check and label all numbers from **1 to 20**.

---

## 2. Factorial of a Number

Write two functions to calculate `n!`.

Example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Requirements:

* Implement one function using a `for` loop.
* Implement another function using a `while` loop.
* Validate the input and handle negative numbers appropriately.

---

## 3. Reverse a Number

Given an integer, reverse its digits.

Example:

```text
Input:  12345
Output: 54321
```

Requirements:

* Use a `while` loop.
* Use only arithmetic operations such as:

    * `% 10`
    * `// 10`
* Handle negative numbers correctly.

---

## 4. Palindrome Checker

### 4.1 Integer Palindrome

Write a function to check whether an integer is a palindrome.

Example:

```text
12321 → Palindrome
12345 → Not a palindrome
```

Use the reverse-number logic from Problem 3.

### 4.2 String Palindrome

Write a second function to check whether a string is a palindrome.

Example:

```text
"racecar" → Palindrome
"hello"   → Not a palindrome
```

Requirements:

* Use a two-pointer approach.
* Use a `while` loop.
* Compare characters from both ends toward the center.

---

## 5. Sum of Digits

Write a program using a `while` loop that takes an integer and calculates the sum of its individual digits.

Example:

```text
Input:  456
Output: 15

Because:
4 + 5 + 6 = 15
```

---

## 6. Armstrong Number Checker

Write a program using a `while` loop to determine whether a number is an **Armstrong number**.

An `n`-digit number is an Armstrong number if the sum of each digit raised to the power `n` equals the original number.

Example:

```text
153 = 1³ + 5³ + 3³
    = 1 + 125 + 27
    = 153
```

Therefore:

```text
153 → Armstrong number
```

---

## 7. Prime Number Range Finder

Using a **nested `for` loop**, find and display all prime numbers between **1 and 50**.

Requirements:

* Use nested loops.
* Use `break` when a number is determined to be non-prime.
* Display all prime numbers in the range.

Expected output:

```text
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

## Practice Progression

Work through the problems in this order:

* [ ] 1. Even or Odd Checker
* [ ] 2. Factorial
* [ ] 3. Reverse a Number
* [ ] 5. Sum of Digits
* [ ] 4. Palindrome Checker
* [ ] 6. Armstrong Number Checker
* [ ] 7. Prime Number Range Finder


