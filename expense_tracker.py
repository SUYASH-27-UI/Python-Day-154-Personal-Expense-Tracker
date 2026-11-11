
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

FIELDS = ["date", "category", "description", "amount"]


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        return list(csv.DictReader(file))


def add_expense():
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))

        if not category or not description or amount <= 0:
            print("Please enter valid expense details.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writerow({
                "date": date.today().isoformat(),
                "category": category,
                "description": description,
                "amount": amount
            })

        print("Expense added successfully.")

    except ValueError:
        print("Enter a valid amount.")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- ALL EXPENSES ---")

    for item in expenses:
        print(
            f"{item['date']} | {item['category']} | "
            f"{item['description']} | Rs. {float(item['amount']):.2f}"
        )


def total_expenses():
    expenses = load_expenses()

    total = sum(float(item["amount"]) for item in expenses)

    print(f"\nTotal Expenses: Rs. {total:.2f}")


def category_summary():
    expenses = load_expenses()
    summary = {}

    for item in expenses:
        category = item["category"]
        amount = float(item["amount"])

        summary[category] = summary.get(category, 0) + amount

    print("\n--- CATEGORY SUMMARY ---")

    if not summary:
        print("No expenses recorded.")
        return

    for category, amount in summary.items():
        print(f"{category}: Rs. {amount:.2f}")


def search_category():
    expenses = load_expenses()
    search = input("Enter category to search: ").strip().lower()

    found = False
    total = 0

    print("\n--- SEARCH RESULTS ---")

    for item in expenses:
        if item["category"].lower() == search:
            amount = float(item["amount"])
            total += amount
            found = True

            print(
                f"{item['date']} | {item['description']} | "
                f"Rs. {amount:.2f}"
            )

    if found:
        print(f"Category Total: Rs. {total:.2f}")
    else:
        print("No expenses found in this category.")


def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Search Category")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            search_category()
        elif choice == "6":
            print("Expense tracker closed.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
