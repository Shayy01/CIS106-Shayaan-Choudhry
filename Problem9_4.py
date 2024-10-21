def compute_ticket_price(miles):
    """Determine the ticket price based on miles from downtown Chicago."""
    if miles >= 30:
        return 12
    elif 20 <= miles < 30:
        return 10
    elif 10 <= miles < 20:
        return 8
    else:
        return 5

def main():
    total_ticket_price = 0

    while True:
        user_input = input("Would you like to enter ticket data? (Yes or No): ").strip().lower()
        if user_input == 'yes':
            last_name = input("Enter your last name: ")
            miles = float(input("Enter miles from downtown Chicago: "))

            ticket_price = compute_ticket_price(miles)
            total_ticket_price += ticket_price

            print(f"{last_name}, your ticket price is: ${ticket_price:.2f}")
        elif user_input == 'no':
            print("Thank you for using the train ticket calculator!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    print(f"\nTotal price of all tickets: ${total_ticket_price:.2f}")

if __name__ == "__main__":
    main()
