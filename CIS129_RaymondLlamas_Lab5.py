# Declare variables
total_bottles = 0
today_bottles = 0
counter = 0  # Initialize counter to 0
NBR_OF_DAYS = 7  # Constant for number of days
total_payout = 0
keep_going = "y"

while keep_going.lower() == "y":
    # Loop for 7 days to get bottles returned
    while counter < NBR_OF_DAYS:
        print(f"Enter number of bottles returned for day #{counter + 1}:")
        today_bottles = int(input())
        total_bottles += today_bottles
        counter += 1  # Add to the counter

    # Calculate total payout
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Print total bottles and total payout
    print(f"Total number of bottles collected: {total_bottles}")
    print(f"Total payout: ${total_payout:.2f}")

    # Reset variables for next run
    total_bottles = 0
    total_payout = 0
    counter = 0

    # Ask user if they want to run the program again
    keep_going = input("Do you want to run the program again? (y/n): ")
