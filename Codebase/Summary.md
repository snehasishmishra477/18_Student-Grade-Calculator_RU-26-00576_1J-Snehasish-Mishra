# Student Grade Calculator

**PS No. 18** | Rungta International Skills University | School of Computer Science and Engineering | B.Tech CSE

## Overview

A console program in Python 3 that takes a student's name and marks in five subjects, then shows the total, percentage, grade and pass/fail result. A loop lets any number of students be entered in one run. Marks are out of 100 per subject, and a student passes with 40% or more.

## Grading Scale

| Percentage | Grade |
|---|---|
| 85 or more | A |
| 70 to below 85 | B |
| 55 to below 70 | C |
| 40 to below 55 | D |
| Below 40 | F |

## How It Works

- Ask for the student name, then the marks of five subjects.
- Each mark is validated in a loop: it must be a whole number from 0 to 100, otherwise an error is shown and the same subject is asked again.
- `calculate_total()` adds the five marks; `calculate_percentage()` divides the total by 5.
- `calculate_grade()` uses if-elif-else to return A, B, C, D or F; the result is Pass at 40% or more, otherwise Fail.
- The result is printed on one line, then the program asks `Another student? (y/n)`; any answer other than `y` ends it.

## Functions

| Function | Purpose |
|---|---|
| `calculate_total(marks)` | Returns the sum of the five marks |
| `calculate_percentage(total)` | Returns total divided by 5 |
| `calculate_grade(percentage)` | Returns A, B, C, D or F |

## Test Results

The program was run against the four required test cases and all four match the expected output.

| # | Scenario | Result |
|---:|---|---|
| 1 | Aman: 80, 70, 90, 60, 50 | Total 350, 70.00%, Grade B, Pass |
| 2 | Neha: 40, 40, 40, 40, 40 (boundary) | Total 200, 40.00%, Grade D, Pass |
| 3 | Ravi, subject 2: 105, abc, then 75 | Two invalid-marks messages, then 75 accepted |
| 4 | Riya: 95, 88, 92, 90, 85; Karan: 30, 35, 40, 25, 20 | Riya 450, 90.00%, A, Pass; Karan 150, 30.00%, F, Fail |

## Limitations and Next Steps

- Marks must be whole numbers; decimals are rejected.
- The subject count is fixed at five and subjects are not named.
- Results are printed only, not saved to a file.
- Future work: name the subjects, accept decimals, save results to CSV, print a class summary.

**Concepts used:** variables, conditions, functions, loops, exception handling.
