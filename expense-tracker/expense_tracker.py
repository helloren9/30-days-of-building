from expense import Expense
import datetime
import calendar


def main():
    print("Running Expense Tracker.")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense.
    expense = get_user_expense()

    # Write the expense to file.
    save_user_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense.
    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    print("Getting user expense.")
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        try:
            selected_index = int(input("Enter a category number: ")) - 1
            selected_category = expense_categories[selected_index]
            break
        except (ValueError, IndexError):
            print("Invalid category. Please try again.")
        
    return Expense(expense_name, selected_category, expense_amount)

def save_user_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print("Summarize user expense.")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")

            if len(parts) != 3:
                continue

            expense_name, expense_amount, expense_category = parts

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")

    today = datetime.date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = days_in_month - today.day
    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: ${daily_budget:.2f}")

if __name__ == "__main__":
    main()