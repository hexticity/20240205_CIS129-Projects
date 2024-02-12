# This program calculates the total cost of items purchased by the user
# at a coffee shop, including tax.

# Define the prices of items as constants
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
CROISSANT_PRICE = 6
BAGEL_PRICE = 3

# Define the tax rate
TAX_RATE = 0.06

# Ask the user how many of each item they want to buy
num_coffees = int(input("How many coffees would you like to buy?\n"))
num_muffins = int(input("How many muffins would you like to buy?\n"))
num_croissants = int(input("How many croissants would you like to buy?\n"))
num_bagels = int(input("How many bagels would you like to buy?\n"))

# Calculate the subtotal by multiplying the number of items by their respective prices
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE) + (num_croissants * CROISSANT_PRICE) + (num_bagels * BAGEL_PRICE)

# Calculate the tax amount by multiplying the subtotal by the tax rate
tax = subtotal * TAX_RATE

# Calculate the total cost by adding the subtotal and tax
total = subtotal + tax

# Display the receipt
print('*' * 39)
print("My Coffee and Muffin Shop")
print('*' * 39)
print("Number of items bought:")
print("Coffee:", num_coffees)
print("Muffins:", num_muffins)
print("Croissants:", num_croissants)
print("Bagels:", num_bagels)
print('*' * 39)
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{num_croissants} Croissants at ${CROISSANT_PRICE} each: ${num_croissants * CROISSANT_PRICE:.2f}")
print(f"{num_bagels} Bagels at ${BAGEL_PRICE} each: ${num_bagels * BAGEL_PRICE:.2f}")
print(f"{TAX_RATE * 100}% tax: ${tax:.2f}")
print('-' * 9)
print(f"Total: ${total:.2f}")
print('*' * 39)

# Thank the user and invite them to visit again
print("Thank you for choosing My Coffee and Muffin Shop!")
print("We appreciate your business and look forward to serving you again soon.")
