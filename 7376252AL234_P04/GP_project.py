def menu():
    print("===== GROCERY LIST AND BUDGET PLANNER =====")
    print("1. Add grocery item")
    print("2. Mark item as bought")
    print("3. Edit item")
    print("4. Remove item")
    print("5. Display grocery list")
    print("6. Set monthly budget")
    print("7. Show three most expensive items")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        return None

    if not (1 <= choice <= 8):
        print("Invalid input. Please enter a number between 1 and 8.")
        return None

    return choice

def load_items():
    try:
        with open("grocery.txt", "r") as file:
            for line in file:
                fields = line.strip().split("|")

                if len(fields) != 6 or fields[0] == "Item":
                    continue

                try:
                    name, category, qty, unit, price, status = fields
                    quantity = int(qty)
                    price_per_unit = float(price)

                    if quantity <= 0 or price_per_unit <= 0:
                        continue

                    item_list[name.lower()] = {
                        "category": category,
                        "quantity": quantity,
                        "unit": unit,
                        "price_per_unit": price_per_unit,
                        "price": quantity * price_per_unit,
                        "status": status.upper()
                    }
                except ValueError:
                    print("Skipping invalid grocery record.")

    except FileNotFoundError:
        pass


budget = 4000.0

def load_budget():
    global budget

    try:
        with open("budget.txt", "r") as file:
            saved_budget = float(file.read().strip())
            if saved_budget > 0:
                budget = saved_budget
    except (FileNotFoundError, ValueError):
        budget = 4000.0

item_list = {}
def add_item():
    item_name = input("Enter the name of the grocery item: ")
    # item_price = input("Enter the price of the item: ")
    category = input("Enter the category of the item: ")
    quantity = input("Enter the quantity of the item: ")
    unit = input("Enter the unit of measurement (e.g., kg, L, pcs): ")
    price_per_unit = input("Enter the price per unit: ")
    status = input("Enter the status of the item (True(bought)/False(pending)): ")
    status = status.strip().lower()
    try :
        item_name = item_name.strip().lower()
        category = category.strip().lower()
        # item_price = float(item_price)
        quantity = int(quantity)
        price_per_unit = float(price_per_unit)
        unit = unit.strip().lower()
        if status == "true":
            status = True
        elif status == "false": 
            status = False
        else:
            print("Invalid status. Please enter 'True' or 'False'.")
            return
        if unit not in ['kg', 'l', 'pcs']:
            print("Invalid unit of measurement. Please enter 'kg', 'L', or 'pcs'.")
            return
        elif quantity <= 0 or price_per_unit <= 0:
            print("Quantity and price per unit must be positive numbers.")
            return
        elif item_name == "" or category == "":
            print("Item name and category cannot be empty.")
            return
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    if item_name not in item_list:
        
        item_list[item_name] = {
            "category": category,
            "quantity": quantity,
            "unit": unit,
            "price_per_unit": price_per_unit,
            "price": quantity * price_per_unit,
            "status": "bought" if status else "pending"
        }
        save_items()
        print(f"Item '{item_name}' added successfully.")
    else:
        item_list[item_name]["quantity"] += quantity
        item_list[item_name]["unit"] = unit
        item_list[item_name]["price_per_unit"] = price_per_unit
        item_list[item_name]["status"] = "bought" if status else "pending"
        item_list[item_name]["category"] = category
        item_list[item_name]["price"] = item_list[item_name]["quantity"] * price_per_unit
        save_items()
        print(f"Item '{item_name}' updated successfully.")
    # print(f"Current grocery list: {item_list}")

def save_items():
    with open("grocery.txt", "w") as file:
        file.write("Item|Category|Quantity|Unit|PricePerUnit|Status\n")

        for item_name, details in item_list.items():
            file.write(
                f"{item_name}|{details['category']}|"
                f"{details['quantity']}|{details['unit']}|"
                f"{details['price_per_unit']}|{details['status']}\n"
            )

def mark_item_bought():
    item_name = input("Enter the name of the item to mark as bought: ")
    item_name = item_name.strip().lower()
    if item_name in item_list:
        item_list[item_name]["status"] = "bought"
        save_items()
        print(f"Item '{item_name}' marked as bought.")
    else:
        print(f"Item '{item_name}' not found in the grocery list.")
    save_items()

def edit_item():
    item_name = input("Enter the name of the item to edit: ")
    item_name = item_name.strip().lower()
    if item_name in item_list:
        print(f"Current details of '{item_name}': {item_list[item_name]}")
        new_category = input("Enter the new category (leave blank to keep current): ")
        new_quantity = input("Enter the new quantity (leave blank to keep current): ")
        new_unit = input("Enter the new unit (leave blank to keep current): ")
        new_price_per_unit = input("Enter the new price per unit (leave blank to keep current): ")
        new_status = input("Enter the new status (True/False, leave blank to keep current): ")

        if new_category:
            item_list[item_name]["category"] = new_category.strip().lower()
        if new_quantity:
            try:
                item_list[item_name]["quantity"] = int(new_quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                return
        if new_unit:
            item_list[item_name]["unit"] = new_unit.strip().lower()
        if new_price_per_unit:
            try:
                item_list[item_name]["price_per_unit"] = float(new_price_per_unit)
            except ValueError:
                print("Invalid price per unit. Please enter a valid number.")
                return
        if new_status:
            if new_status.strip().lower() == "true":
                item_list[item_name]["status"] = "bought"
            elif new_status.strip().lower() == "false":
                item_list[item_name]["status"] = "pending"
            else:
                print("Invalid status. Please enter 'True' or 'False'.")
                return

        # Update the total price after editing
        item_list[item_name]["price"] = item_list[item_name]["quantity"] * item_list[item_name]["price_per_unit"]
        save_items()
        print(f"Item '{item_name}' updated successfully.")
    else:
        print(f"Item '{item_name}' not found in the grocery list.")

def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    item_name = item_name.strip().lower()
    if item_name in item_list:
        del item_list[item_name]
        save_items()
        print(f"Item '{item_name}' removed successfully.")
    else:
        print(f"Item '{item_name}' not found in the grocery list.")

def display_list():
    if not item_list:
        print("The grocery list is empty.")
        return

    planned_total = 0
    bought_total = 0
    categories = {}

    for name, details in item_list.items():
        category = details["category"]
        amount = details["quantity"] * details["price_per_unit"]

        planned_total += amount

        if details["status"].upper() == "BOUGHT":
            bought_total += amount

        if category not in categories:
            categories[category] = []

        categories[category].append((name, details, amount))

    print("\n===== GROCERY LIST BY CATEGORY =====")

    for category, items in categories.items():
        print(f"\nCategory: {category}")

        for name, details, amount in items:
            print(f"Item: {name}")
            print(f"Quantity: {details['quantity']} {details['unit']}")
            print(f"Price per unit: {details['price_per_unit']:.2f}")
            print(f"Total price: {amount:.2f}")
            print(f"Status: {details['status']}")
            print("------------------------")

    remaining = budget - planned_total

    print(f"\nPlanned total: {planned_total:.2f}")
    print(f"Bought total: {bought_total:.2f}")
    print(f"Monthly budget: {budget:.2f}")
    print(f"Remaining budget: {remaining:.2f}")

    if remaining < 0:
        print(f"WARNING: Budget exceeded by {abs(remaining):.2f}")

def set_budget():
    global budget

    value = input("Enter your monthly budget: ")

    try:
        value = float(value)

        if value <= 0:
            print("Budget must be a positive number.")
            return

        budget = value

        with open("budget.txt", "w") as file:
            file.write(str(budget))

        print(f"Monthly budget set to Rs. {budget:.2f}.")

        planned_total = sum(
            details["quantity"] * details["price_per_unit"]
            for details in item_list.values()
        )

        if planned_total > budget:
            print("WARNING: Planned spending exceeds your budget!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def show_most_expensive_items():
    if not item_list:
        print("The grocery list is empty.")
        return

    sorted_items = sorted(item_list.items(), key=lambda x: x[1]["price"], reverse=True)
    top_items = sorted_items[:3]

    print("===== THREE MOST EXPENSIVE ITEMS =====")
    for item_name, details in top_items:
        print(f"Item: {item_name}")
        print(f"  Category: {details['category']}")
        print(f"  Quantity: {details['quantity']} {details['unit']}")
        print(f"  Price per Unit: ${details['price_per_unit']:.2f}")
        print(f"  Total Price: ${details['price']:.2f}")
        print(f"  Status: {details['status']}")
        print("------------------------")

def main():
    load_items()
    load_budget()
    while True:
        choice = menu()
        if choice == 1:
            add_item()
        elif choice == 2:
            mark_item_bought()
        elif choice == 3:
            edit_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            display_list()
        elif choice == 6:
            set_budget()
        elif choice == 7:
            show_most_expensive_items()
        elif choice == 8:
            print("Exiting the program. Goodbye!")
            break
    
if __name__ == "__main__":
    main()