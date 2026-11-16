# Student Grade Calculator

**PS No. 18** | Rungta International Skills University
School of Computer Science and Engineering | B.Tech Computer Science and Engineering

A console-based Python 3 program that takes a student's marks in five subjects, calculates the total, percentage, grade and pass/fail result, and lets you enter more students through a loop.

---

## Problem Statement

Create a program that takes a student's marks in five subjects, calculates the total, percentage, grade and pass/fail result, and allows more students to be entered through a loop.

- Marks are out of 100 in each of the five subjects.
- A student **passes** with **40% or more**.

### Grading Scale

| Percentage | Grade |
|------------|-------|
| >= 85      | A     |
| >= 70      | B     |
| >= 55      | C     |
| >= 40      | D     |
| below 40   | F     |

---

## Features

- Takes the student name and marks of five subjects as input
- Calculates total and percentage using separate functions
- Assigns a grade using `if-elif-else`
- Decides the Pass/Fail result (40% pass limit)
- Validates marks (only numbers from 0 to 100 are accepted)
- Re-asks for a subject's marks on invalid input without losing earlier entries
- Loops to allow multiple students

## Concepts Used

- Variables
- Conditions (`if`, `elif`, `else`)
- Functions (`calculate_total()`, `calculate_percentage()`, `calculate_grade()`)
- Loops (`while`, `for`)
- Exception handling (`try` / `except`)

---

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python student_grade_calculator.py
```

(Use `python3` instead of `python` if required on your system.)

---

## Program Flow

1. Enter the student's name.
2. Enter marks for each of the five subjects (validated, 0 to 100).
3. The program calculates the total, percentage, grade and result.
4. The result is displayed.
5. The program asks `Another student? (y/n)`. Entering `y` repeats the process; `n` exits.

## Functions

| Function | Description |
|----------|-------------|
| `calculate_total(marks)` | Returns the sum of the five subject marks |
| `calculate_percentage(total)` | Returns the percentage (`total / 5`) |
| `calculate_grade(percentage)` | Returns the grade (A, B, C, D or F) |

---

## Test Cases

### Test Case 1: Normal Input
**Input**
```
Name: Aman
Marks: 80, 70, 90, 60, 50
```
**Expected Output**
```
Aman | Total: 350 | Percentage: 70.00% | Grade: B | Result: Pass
```

### Test Case 2: Boundary / Minimum Input
**Input**
```
Name: Neha
Marks: 40, 40, 40, 40, 40
```
**Expected Output**
```
Neha | Total: 200 | Percentage: 40.00% | Grade: D | Result: Pass
```

### Test Case 3: Invalid Input
**Input**
```
Name: Ravi
Marks for subject 2: 105, then abc, then 75
```
**Expected Output**
```
Invalid marks. Enter a number between 0 and 100.
Invalid marks. Enter a number between 0 and 100.
(Second subject is accepted as 75)
```

### Test Case 4: Different Valid Scenario
**Input**
```
(a) Name: Riya; Marks: 95, 88, 92, 90, 85
    Another student? y
(b) Name: Karan; Marks: 30, 35, 40, 25, 20
```
**Expected Output**
```
Riya | Total: 450 | Percentage: 90.00% | Grade: A | Result: Pass
Karan | Total: 150 | Percentage: 30.00% | Grade: F | Result: Fail
```

---

## Project Structure

```
.
├── student_grade_calculator.py
└── README.md
```

## Author

- Name: Snehasish Mishra
- Enrollment No: RU-26-00576
- Program: B.Tech Computer Science(AI ML)
- University: Rungta International Skills University
