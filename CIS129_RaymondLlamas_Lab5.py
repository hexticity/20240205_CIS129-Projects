# Project: Lab 5 The Bottle Return Program
# Author: Raymond Llamas
# Date: 02-26-2024

# Program Description: This program calculates the total payout for returning bottles over a week.

# Declare variables
total_bottles = 0  # Total number of bottles collected for the week
today_bottles = 0  # Number of bottles returned on a particular day
counter = 0  # Counter for loop iteration
NBR_OF_DAYS = 7  # Constant for number of days in a week
total_payout = 0  # Total payout for the week
keep_going = "y"  # Control variable for running the program again

# Main loop to run the program
while keep_going.lower() == "y":
    # Loop to get the number of bottles returned for each day of the week
    while counter < NBR_OF_DAYS:
        print(f"Enter number of bottles returned for day #{counter + 1}:")
        today_bottles = int(input())
        total_bottles += today_bottles
        counter += 1  # Increment the counter

    # Calculate total payout for the week
    PAYOUT_PER_BOTTLE = 0.10  # Payout per bottle
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Display total bottles collected and total payout for the week
    print(f"Total number of bottles collected for the week: {total_bottles}")
    print(f"Total payout for the week: ${total_payout:.2f}")

    # Reset variables for next run
    total_bottles = 0
    total_payout = 0
    counter = 0

    # Ask user if they want to run the program again
    keep_going = input("Do you want to run the program again? (y/n): ")
