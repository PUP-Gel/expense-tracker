# Expense-Tracker - Installment 4
# Author: Stephen Nigel A. Cabaluna
# A personal expense tracker landing page

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print()

print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")
elif amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2 
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = bool(total > budget)
left = budget - total


print("-" * 40)
print("SUMMARY")
print(f"    - {item1}:\t${amount1}")
print(f"    - {item2}:\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand total:\t\t${total}")

if over_budget:
    over_amount = total - budget
    print(f"Over by ${over_amount}!")
elif total > (budget * 0.9):
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print("Made by: Stephen Nigel A. Cabaluna  |  Installment 4")
