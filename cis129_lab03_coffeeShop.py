# This program calculates the total cost of coffee and muffins purchased by the user,
# including tax. The price of a cup of coffee is $5 and the price of a muffin is $4.

# Define the prices of coffee and muffin as constants
COFFEE_PRICE = 5
MUFFIN_PRICE = 4

# Define the tax rate
TAX_RATE = 0.06

# Ask the user how many coffees and muffins they want to buy
num_coffees = int(input("How many coffees would you like to buy?\n"))
num_muffins = int(input("How many muffins would you like to buy?\n"))

# Calculate the subtotal by multiplying the number of items by their respective prices
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE)

# Calculate the tax amount by multiplying the subtotal by the tax rate
tax = subtotal * TAX_RATE

# Calculate the total cost by adding the subtotal and tax
total = subtotal + tax

# Display the receipt
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(num_coffees)
print("Number of muffins bought?")
print(num_muffins)
print("***************************************")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{TAX_RATE * 100}% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")