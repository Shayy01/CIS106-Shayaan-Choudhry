def get_discount_percent(make, model, ev_code):
    """Determine the discount percent based on vehicle make, model, and EV status."""
    if make == "Honda" and model == "Accord":
        return 0.10
    elif make == "Toyota" and model == "Rav4":
        return 0.15
    elif ev_code.upper() == "Y":
        return 0.30  # All electric vehicles
    else:
        return 0.05  # All other vehicles

def compute_out_the_door_price(msrp, make, model, ev_code):
    """Compute the out-the-door price of the automobile."""
    discount_percent = get_discount_percent(make, model, ev_code)
    discount_amount = msrp * discount_percent
    new_msrp = msrp - discount_amount
    sales_tax = new_msrp * 0.07
    total_price = new_msrp + sales_tax
    return total_price

def main():
    total_msrp = 0
    total_sales_price = 0

    while True:
        user_input = input("Would you like to enter automobile data? (Yes or No): ").strip().lower()
        if user_input == 'yes':
            make = input("Enter the make of the automobile: ")
            model = input("Enter the model of the automobile: ")
            ev_code = input("Is it an electric vehicle? (Y or N): ").strip()
            msrp = float(input("Enter the MSRP (sticker pr    ice): "))

            total_msrp += msrp
            out_the_door_price = compute_out_the_door_price(msrp, make, model, ev_code)
            total_sales_price += out_the_door_price

            print(f"The out-the-door price for the {make} {model} is: ${out_the_door_price:.2f}")
        elif user_input == 'no':
            print("Thank you for using the automobile pricing calculator!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    print(f"\nTotal MSRP of all vehicles: ${total_msrp:.2f}")
    print(f"Total sales price of all vehicles: ${total_sales_price:.2f}")

if __name__ == "__main__":
    main()
