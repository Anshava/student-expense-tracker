import json

expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    description = input("Enter expense description: ")
    amount = float(input("Enter amount: ₹"))

    print("\nChoose a category:")
    print("1. Food")
    print("2. Travel")
    print("3. Study")
    print("4. Entertainment")
    print("5. Other")

    choice = input("Enter category number: ")

    categories = {
        "1": "Food",
        "2": "Travel",
        "3": "Study",
        "4": "Entertainment",
        "5": "Other"
    }

    category = categories.get(choice, "Other")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("✅ Expense added successfully!")


def view_expenses():
    print("\n--- Your Expenses ---")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    total = 0

    for i, expense in enumerate(expenses, 1):
        print(f"\n{i}. {expense['description']}")
        print(f"   Amount: ₹{expense['amount']}")
        print(f"   Category: {expense['category']}")

        total += expense["amount"]

    print(f"\n💰 Total Expenses: ₹{total}")


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("✅ Expenses saved successfully!")


while True:
    print("\n===== STUDENT EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        save_expenses()

    elif choice == "4":
        print("Thank you for using Student Expense Tracker! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")