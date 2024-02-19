# Module 04 Lab-04
# Author: Raymond Llamas
# Date: 2024-02-18
# Program Description: 


# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = "Enter the monthly sales amount: " # prompt will be a string literal

# include code to get the monthly Sales
monthlySales = float(input(prompt))

# include code to get the Increase in Sales
salesIncrease = float(input("Enter the percent of increase in sales (in decimal format): "))
salesIncrease = salesIncrease / 100  # Convert to decimal

# include code to Calculate the Store Bonus (storeAmount)
if monthlySales > 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# include code to Calculate the Employee Bonus (empAmount)
if salesIncrease >= .05:
  empAmount = 75
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible! ')
