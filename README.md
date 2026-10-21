# GROCERY LIST AND BUDGET PLANNER

## 1. Project Description
The Grocery List and Budget Planner is a menu-driven Python application that helps users manage grocery items and track monthly grocery expenses. It allows users to add, edit, remove, and mark items as bought. It also calculates planned spending and compares it with the monthly budget.

## 2. Features
- Add grocery items with name, category, quantity, unit, and price per unit.
- Mark grocery items as bought.
- Edit existing grocery item details.
- Remove items from the grocery list.
- Display grocery items grouped by category.
- Set and save a monthly budget.
- Calculate total planned spending and bought-item expenses.
- Display the most expensive grocery items.
- Warn users when planned spending exceeds the budget.
- Store grocery and budget data in text files for future use.
- Validate user input to reduce errors.

## 3. Technologies Used
- Programming Language: Python
- Concepts: Functions, dictionaries, loops, conditional statements, exception handling, file handling, and input validation.
- Storage: Pipe-separated text files.
- External Libraries: None.

## 4. Files Used
- `main.py` – Contains the Python program. (Use your actual Python filename if different.)
- `grocery.txt` – Stores grocery item records.
- `budget.txt` – Stores the monthly budget.
- `README.txt` – Contains project documentation.
- `sample_run.txt` – Contains sample program execution.

## 5. How to Run
1. Install Python 3 on your computer.
2. Place the Python program, `grocery.txt`, and `budget.txt` in the same folder.
3. Open a terminal or command prompt in that folder.
4. Run the following command:

   `python main.py`

5. Select an option from the menu and follow the instructions displayed on the screen.

## 6. Data Format
Grocery records are stored in `grocery.txt` using the pipe (`|`) separator.

Example header:

`Item|Category|Quantity|Unit|PricePerUnit|Status`

Each record contains the item name, category, quantity, unit, price per unit, and purchase status.

The monthly budget is stored in `budget.txt`.

## 7. Input Validation
The application checks user input such as menu choices, numeric quantities, prices, and purchase status. Invalid inputs should be corrected according to the messages displayed by the program.

## 8. Limitations
- Data is stored in local text files.
- The application runs in a terminal and does not have a graphical user interface.
- It is designed for a single user.
- Data files must remain in the correct folder for the program to load saved records.

## 9. Conclusion
The Grocery List and Budget Planner provides a simple way to organize grocery purchases, maintain item records, and monitor spending against a monthly budget. The project demonstrates fundamental Python programming and file-handling concepts.