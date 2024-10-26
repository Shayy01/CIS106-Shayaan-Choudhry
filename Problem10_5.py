# Declare global variables for total and tax
total = 0.0
tax = 0.0

def compute_total_and_tax(quantity, unit_price):
    global total, tax 
    total = quantity * unit_price
    tax = total * 0.07

def main():
    # Input quantity and unit price
    quantity = float(input("Enter quantity of the item: "))
    unit_price = float(input("Enter unit price: "))

    # Compute total and tax
    compute_total_and_tax(quantity, unit_price)

    # Display results
    print(f"\nTotal: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")

if __name__ == "__main__":
    main()
