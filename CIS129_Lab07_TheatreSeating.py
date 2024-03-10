# Constants
SECTION_NAMES = ['A', 'B', 'C']
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}
SEAT_CAPACITY = {'A': 300, 'B': 500, 'C': 200}

def display_welcome_message():
    print("Welcome to the Theater Seating Program!")
    print("Section Names:", SECTION_NAMES)
    print("Seat Prices:", SEAT_PRICES)
    print("Seat Capacity:", SEAT_CAPACITY)
    print()

def get_ticket_sales():
    ticket_sales = {}
    for section in SECTION_NAMES:
        while True:
            try:
                tickets_sold = int(input(f"Enter the number of tickets sold for section {section}: "))
                if tickets_sold < 0 or tickets_sold > SEAT_CAPACITY[section]:
                    print("Invalid input. Please enter a non-negative number not exceeding the seat capacity.")
                else:
                    ticket_sales[section] = tickets_sold
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return ticket_sales

def calculate_total_sales(ticket_sales):
    total_sales = 0
    for section, tickets_sold in ticket_sales.items():
        total_sales += tickets_sold * SEAT_PRICES[section]
    return total_sales

def display_sales_summary(ticket_sales, total_sales):
    print("\nSales Summary:")
    for section, tickets_sold in ticket_sales.items():
        print(f"Section {section}: {tickets_sold} tickets sold. Subtotal: ${tickets_sold * SEAT_PRICES[section]}")
    print(f"\nOverall Total Sales: ${total_sales}")

def main():
    display_welcome_message()
    ticket_sales = get_ticket_sales()
    total_sales = calculate_total_sales(ticket_sales)
    display_sales_summary(ticket_sales, total_sales)

if __name__ == "__main__":
    main()