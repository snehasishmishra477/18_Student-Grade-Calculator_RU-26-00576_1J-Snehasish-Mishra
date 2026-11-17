# Bus Pass Management System

**PS No. 62** | Rungta International Skills University | School of Computer Science and Engineering | B.Tech CSE

## Overview

A console application in Python 3 that issues and manages bus passes. Users can issue, renew, search, view, edit and delete passes. The fee depends on the pass type and the passenger category, and every pass is saved in `buspass.txt` so the data is kept between runs.

## Pass Types and Fees

| Pass type | Validity | General fee | Student fee (25% off) |
|---|---:|---:|---:|
| Monthly | 30 days | Rs. 500 | Rs. 375 |
| Quarterly | 90 days | Rs. 1350 | Rs. 1012.5 |
| Yearly | 365 days | Rs. 4800 | Rs. 3600 |

## How It Works

- Passes are held in a list; each pass is a dictionary (`id`, `name`, `route`, `type`, `category`, `fee`, `validity`).
- Pass types and base fees are kept in a dictionary, so a fee is a simple lookup; students get 25% off.
- `load_passes()` reads `buspass.txt` (JSON) at start; `save_passes()` writes it after every change.
- `generate_id()` returns the next ID after the highest existing one, starting at BP101, so IDs never repeat.
- Empty name or route, an unknown pass type and an unknown category are rejected and nothing is saved.

## Menu and Functions

| Option | Action | Function |
|---:|---|---|
| 1 | Issue a new pass | `issue_pass()` |
| 2 | Renew an existing pass | `renew_pass()` |
| 3 | Search a pass by ID | `search_pass()` |
| 4 | View all passes | `view_passes()` |
| 5 | Exit | `main()` |
| 6 | Edit an existing pass | `edit_pass()` |
| 7 | Delete an existing pass (with confirmation) | `delete_pass()` |

## Test Results

The program was run against the four required test cases. The behaviour and saved data match in all four.

| # | Scenario | Result |
|---:|---|---|
| 1 | Issue Riya, Route 5, Monthly, General | BP101, Rs. 500, 30 days: passed |
| 2 | Empty file, view all | "No passes issued yet.": passed |
| 3 | Issue with type Weekly | "Invalid pass type!", pass not issued: passed (wording differs) |
| 4 | Issue Aman, Yearly, Student; search BP101 | BP102, Rs. 3600.0, 365 days; BP101 found from the saved file: passed |

## Limitations and Next Steps

- Editing the category does not recalculate the fee.
- No issue or expiry date is stored, so expiry cannot be checked.
- A damaged `buspass.txt` would stop the program on start.
- Future work: store dates, recalculate fees on edit, handle bad files, add reports by route.

**Concepts used:** lists, dictionaries, functions, file handling (`json`, `os`).
