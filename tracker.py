# Expense-Tracker - Installment 5
# Author: Stephen Nigel A. Cabaluna
# A personal expense tracker landing page

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print()

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0

print()
print("MAIN MENU")
print("\t[1] Add an expense")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent")
print("\t[4] Exit")

while True:
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        average = subtotal / count if count > 0 else 0
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        over_budget = total > budget

        print(f"  Expenses:\t\t    {count}")
        print(f"  Subtotal:\t\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t\t${tax}")
        print(f"  Grand total:\t\t${total}")

        if over_budget:
            over_amount = total - budget
            print(f"  Over by ${over_amount}!")
        elif total > (budget * 0.9):
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Stephen Nigel A. Cabaluna  |  Installment 5")
        print("=" * 40)
        break

    else:
        print("  Please choose 1, 2, 3 or 4.")