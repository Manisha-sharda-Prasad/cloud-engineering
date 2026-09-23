# Python Practice Questions

## 🟢 Tier 1: Basic Input, Math, & String Formatting (Questions 1–4)

### Question 1: Ounces to Pounds Conversion

Write a program that takes a floating-point number representing ounces from the user input. Convert those ounces to pounds (`1 pound = 16 ounces`).
Output the result rounded to exactly **two decimal places**.

* **Example Input:** `42.5`
* **Expected Output:** `2.66 pounds`

---

### Question 2: Acronym Generator

Write a program that reads a line of input containing three words separated by spaces. 
Output an acronym made of the first letter of each word in uppercase.

* **Example Input:** `central intelligence agency`
* **Expected Output:** `CIA`

---

### Question 3: Dynamic Greeting with Stripping

Write a program that reads a user's name from input. The input might accidentally contain leading or trailing whitespace. 
Clean the whitespace and output a greeting exactly as shown below.

* **Example Input:** `   Alex Smith   `
* **Expected Output:** `Hello Alex Smith, welcome!`

---

### Question 4: Simple Integer Math

Write a program that reads four integers from input, each on a new line. 
Output the product of the first two numbers subtracted by the sum of the last two numbers.

**Example Input:**

```text
5
4
3
2
```

**Expected Output:**

```text
15
```

**Explanation:** `(5 * 4) - (3 + 2) = 20 - 5 = 15`

---

## 🟡 Tier 2: Branching & Basic Loop Logic (Questions 5–8)

### Question 5: Interstate Highway Logic

Write a program that reads an integer representing a highway number.

* If the number is between **1 and 99** (inclusive), it is a primary highway. Output:
  `Primary highway`

* If the number is between **100 and 999** (inclusive), it is an auxiliary highway. Output:
  `Auxiliary highway`

* For any other number, output:
  `Invalid highway number`

* **Example Input:** `405`

* **Expected Output:** `Auxiliary highway`

---

### Question 6: Character Frequency Filter

Write a program that reads a single character on the first line of input, followed by a phrase on the second line. 
Count how many times that character appears in the phrase (**case-sensitive**).

**Example Input:**

```text
e
Green Elephant
```

**Expected Output:**

```text
3
```

---

### Question 7: Even Number Range Count

Write a program that reads two integers representing a start and end range (inclusive).
Use a loop to count how many **even numbers** exist within that range.

**Example Input:**

```text
4
11
```

**Expected Output:**

```text
4
```

**Explanation:** `4, 6, 8, 10`

---

### Question 8: Sentinel Loop — Stop on Negative

Write a program that continuously reads integers from user input until a **negative integer** is entered. 
Once the negative number is detected, stop reading and output the sum of all the positive integers entered.

**Example Input:**

```text
10
5
23
-1
```

**Expected Output:**

```text
38
```

---

## 🔴 Tier 3: Collections & Data Structures (Questions 9–12)

### Question 9: List Slicing and Reverse Filter

Write a program that reads a single line of space-separated integers into a list.
Output the elements from **index 1 up to index 4** (inclusive of index 4) in **reverse order**, separated by spaces.

* **Example Input:** `10 20 30 40 50 60 70`
* **Expected Output:** `50 40 30 20`

---

### Question 10: Dictionary Key Lookup

You are given a hardcoded inventory dictionary:

```python
items = {
    'apple': 0.99,
    'banana': 0.59,
    'orange': 0.79,
    'kiwi': 1.25
}
```

Write a program that takes an item name as input.

* If the item exists, print its price in the specified format.
* If it does not exist, print a missing message.

**Example Input 1:**

```text
banana
```

**Expected Output 1:**

```text
Price: $0.59
```

**Example Input 2:**

```text
pear
```

**Expected Output 2:**

```text
Not in inventory
```

---

### Question 11: Find the Maximum Value in a Dictionary

Write a program that takes a single line of input containing pairs of names and test scores separated by commas.

**Example format:**

```text
Name Score, Name Score
```

Store the data in a dictionary, find the student with the **highest score**, and print their name.

* **Example Input:** `Sam 85, Tara 94, John 88`
* **Expected Output:** `Top Student: Tara`

---

### Question 12: Parallel List Zipping

Write a program that reads two lines of input.

* The first line contains space-separated string keys.
* The second line contains space-separated integer values.

Combine them into a dictionary and print the sorted dictionary keys along with their values.

**Example Input:**

```text
A B C
10 20 30
```

**Expected Output:**

```text
{'A': 10, 'B': 20, 'C': 30}
```

---

## 🔥 Tier 4: File Handling & Exceptions (Questions 13–15)

### Question 13: Parsing a Text File

Write a program that reads a filename from user input. Open that text file and read its contents. 
Count how many times the word **"Python"** appears in the file, then print the count.

* **Example Input:** `document.txt`
* **Expected Output:** `Total matches: 7`

---

### Question 14: Processing a CSV File

Write a program that reads the name of a CSV file from user input.

The CSV file contains rows of data representing employees and their monthly sales amounts:

```text
Name,Sales
```

Read the file, calculate the **average sales amount**, and print it rounded to two decimal places.

* **Example Input:** `sales.csv`
* **Expected Output:** `Average Sales: 4520.50`

---

### Question 15: Safe File Reading with Exception Handling

Write a program that prompts the user for a filename. Try to open and read the file.

If the file does not exist, instead of letting the program crash, catch the `FileNotFoundError` and output a customized error message.

* **Example Input:** `missing_file.txt`
* **Expected Output:** `Error: The requested file missing_file.txt was not found.`

---

# Summary

| Tier      | Questions | Main Topics                                     |
| --------- | --------: | ----------------------------------------------- |
| 🟢 Tier 1 |       1–4 | Input, math, strings, formatting                |
| 🟡 Tier 2 |       5–8 | `if/elif/else`, loops, counters, sentinel loops |
| 🔴 Tier 3 |      9–12 | Lists, slicing, dictionaries, `zip()`, sorting  |
| 🔥 Tier 4 |     13–15 | Files, CSV, exceptions                          |

**Total Questions: 15**
