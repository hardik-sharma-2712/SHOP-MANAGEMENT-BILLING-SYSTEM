# Shop Billing System

A simple Python console application that generates a bill for a shop, calculates totals, and saves each bill as a timestamped text file.

**Author:** Hardik Sharma
**Registration Number:** 26BAI10723

## Features

- Validated user input for quantity (integer) and price (non-negative float)
- Auto-generates item names (`Item_1`, `Item_2`, ...) if left blank
- Calculates per-item totals and the grand total
- Displays a neatly formatted bill in the console
- Automatically saves every bill as a `.txt` file inside a `bills/` folder, named using the current date and time

## Requirements

- Python 3.x (no external libraries required — uses only the built-in `os` and `datetime` modules)

## How to Run

```bash
python main.py
```

## Usage

1. Enter the number of items to bill.
2. For each item, enter its name, quantity, and price.
3. The program prints a formatted bill with the grand total.
4. The bill is automatically saved to `bills/bill_<YYYYMMDD_HHMMSS>.txt`.

## Example

```
====== SHOP BILLING ======
How many items? : 2

Item 1
Name: Notebook
Qty: 3
Price: 40

Item 2
Name: Pen
Qty: 5
Price: 10

------- BILL -------
Name            Qty   Price   Total
Notebook          3    40.0    120.0
Pen                5    10.0    50.0
--------------------
Grand Total = 170.0
--------------------
Bill saved: bill_20260926_143210.txt
```

## Project Structure

```
.
├── main.py       # Main program
└── bills/        # Auto-created folder storing saved bills (.txt)
```

## Future Improvements

- Add GUI (Tkinter) or web interface
- Store bills in a database instead of text files
- Add tax/discount support
- Export bills directly as PDF receipts
