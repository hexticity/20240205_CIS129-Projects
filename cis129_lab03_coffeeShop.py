"""
Program: Coffee and Muffin Shop
Author: Raymond Llamas
Course: CIS129 (21339)
Professor: Troy Adams
This program calculates the total cost of coffee and muffins purchased by the user,
including tax. The price of a cup of coffee is $5 and the price of a muffin is $4.
"""

# Define constants
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX_RATE = 0.06

# Ask the user for the number of coffees and muffins
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))

# Calculate the subtotal
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE)

# Calculate the tax
tax = subtotal * TAX_RATE

# Calculate the total
total = subtotal + tax

# Display the receipt
print("*" * 39)
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(num_coffees)
print("Number of muffins bought?")
print(num_muffins)
print("*" * 39)
print("*" * 39)
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{TAX_RATE * 100}% tax: ${tax:.2f}")
print("-" * 9)
print(f"Total: ${total:.2f}")
print("*" * 39)
